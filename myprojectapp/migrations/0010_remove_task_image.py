# Generated by Django 4.2.5 on 2023-09-06 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0009_alter_task_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]
