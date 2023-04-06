# Generated by Django 4.1.7 on 2023-04-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], max_length=200, null=True),
        ),
    ]
