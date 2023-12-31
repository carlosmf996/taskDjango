# Generated by Django 4.2.7 on 2023-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
