# Generated by Django 3.2.5 on 2021-07-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoListApp', '0002_task_created2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created2',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
