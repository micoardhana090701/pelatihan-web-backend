# Generated by Django 4.2.5 on 2023-09-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0007_remove_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='task_images/'),
        ),
    ]
