# Generated by Django 4.2.5 on 2023-09-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0005_alter_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(upload_to='task/'),
        ),
    ]
