# Generated by Django 5.1.1 on 2024-09-19 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0022_category_user_alter_todoitem_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todoitem",
            name="category",
        ),
        migrations.AddField(
            model_name="todoitem",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="todo.category",
            ),
        ),
    ]
