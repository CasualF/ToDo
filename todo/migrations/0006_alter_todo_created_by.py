# Generated by Django 4.2.3 on 2023-07-14 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todo", "0005_alter_todo_is_done"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_todos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]