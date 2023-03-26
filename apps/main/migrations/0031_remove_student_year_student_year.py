# Generated by Django 4.1.7 on 2023-03-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_student_aadhaar_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Year',
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default='First', max_length=200, null=True),
        ),
    ]
