# Generated by Django 4.1.7 on 2023-03-15 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_staff_gender_alter_staff_home_contact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], default='CSE', max_length=200),
        ),
        migrations.AlterField(
            model_name='subject',
            name='regulation',
            field=models.CharField(choices=[('2017 regulation', '2017 regulation'), ('2021 regulation', '2021 regulation')], default='2017 regulation', max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second')], default='First', max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default='First', max_length=200),
        ),
        migrations.CreateModel(
            name='TimeTableInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='main.staff')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='main.timetableinfo')),
            ],
        ),
    ]