# Generated by Django 5.1.1 on 2024-09-14 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0007_alter_todo_item_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo_item",
            name="priority",
            field=models.CharField(
                choices=[("3", "High"), ("2", "Medium"), ("1", "Low")]
            ),
        ),
    ]
