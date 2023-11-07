# Generated by Django 4.2.7 on 2023-11-07 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_task_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]