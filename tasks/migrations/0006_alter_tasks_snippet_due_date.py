# Generated by Django 3.2.5 on 2022-01-15 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_tasks_snippet_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks_snippet',
            name='due_date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
