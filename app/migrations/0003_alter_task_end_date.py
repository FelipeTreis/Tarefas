# Generated by Django 4.1.4 on 2023-01-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_task_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="end_date",
            field=models.DateField(blank=True, null=True, verbose_name="Data final"),
        ),
    ]
