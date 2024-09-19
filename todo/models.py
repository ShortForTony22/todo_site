from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models import Case, Value, When
from django.contrib.postgres.search import SearchVector


# Create your models here.
class TodoQuerySet(models.QuerySet):
    def order_by_priority(self):
        return self.alias(
            priority_order=Case(
                When(priority=TodoItem.Priority.HIGH, then=Value(1)),
                When(priority=TodoItem.Priority.MEDIUM, then=Value(2)),
                When(priority=TodoItem.Priority.LOW, then=Value(3)),
            )
        ).order_by("priority_order", "title")

    def order_by_date(self):
        return self.alias().order_by("due_date")


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class TodoItem(models.Model):

    class Priority(models.TextChoices):
        HIGH = "HIGH", _("High")
        MEDIUM = "MEDIUM", _("Medium")
        LOW = "LOW", _("Low")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=Priority.choices)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    objects = TodoQuerySet.as_manager()

    @staticmethod
    def search_by(search_type, search_text, curr_user):
        return (
            TodoItem.objects.filter(user=curr_user)
            .annotate(search=SearchVector(search_type))
            .filter(search=search_text)
        )

    def __str__(self) -> str:
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Is Completed: {self.is_completed}, Priority: {self.priority}, Category: {self.category}"
