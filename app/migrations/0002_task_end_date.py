# Generated by Django 4.1.4 on 2022-12-29 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="end_date",
            field=models.DateField(null=True, verbose_name="Data final"),
        ),
    ]
