# Generated by Django 4.1.7 on 2023-03-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_studentattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='time',
            field=models.TimeField(),
        ),
    ]
