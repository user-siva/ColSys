# Generated by Django 4.1.7 on 2023-03-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_remove_student_year_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='reason',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]