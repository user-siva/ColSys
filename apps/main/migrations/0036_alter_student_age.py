# Generated by Django 4.1.7 on 2023-03-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_remove_studentattendance_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
