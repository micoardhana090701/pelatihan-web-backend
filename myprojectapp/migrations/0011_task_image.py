# Generated by Django 4.2.5 on 2023-09-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0010_remove_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='image/test.png', upload_to='image/'),
        ),
    ]
