# Generated by Django 4.2.5 on 2023-09-07 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0011_task_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='image/test.png', upload_to='image/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myprojectapp.task')),
            ],
        ),
    ]