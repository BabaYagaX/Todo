# Generated by Django 3.2.3 on 2021-06-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
