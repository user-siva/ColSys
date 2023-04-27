# Generated by Django 4.2 on 2023-04-10 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.CharField(blank=True, max_length=5, null=True)),
                ('Employee_Category', models.CharField(blank=True, choices=[('Assistant professor', 'Assistant professor'), ('Professor', 'Professor'), ('Lab Staff', 'Lab Staff'), ('Supporting Staff', 'Supporting Staff'), ('Driver', 'Driver'), ('Maintenance Staff', 'Maintenance Staff')], max_length=30, null=True)),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200, null=True)),
                ('Father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('Home_contact_No', models.IntegerField(blank=True, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10, null=True)),
                ('Blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('Aadhaar_no', models.IntegerField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Date_of_Joining', models.DateField(blank=True, null=True)),
                ('Marital_Status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10, null=True)),
                ('Spouse_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Children_count', models.IntegerField(blank=True, null=True)),
                ('Department', models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], max_length=200)),
                ('Qualification', models.CharField(blank=True, max_length=50, null=True)),
                ('Experience', models.CharField(blank=True, max_length=50, null=True)),
                ('Religion', models.CharField(blank=True, max_length=30, null=True)),
                ('Community', models.CharField(blank=True, choices=[('OC', 'OC'), ('BC', 'BC'), ('MBC', 'MBC'), ('SC\\ST', 'SC\\ST'), ('Other', 'Other')], max_length=10, null=True)),
                ('Door_no', models.IntegerField(blank=True, null=True)),
                ('Street_and_Area', models.CharField(blank=True, max_length=200, null=True)),
                ('District', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.CharField(blank=True, max_length=50, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Office_Door_no', models.IntegerField(blank=True, null=True)),
                ('Office_Street_and_Area', models.CharField(blank=True, max_length=200, null=True)),
                ('Office_District', models.CharField(blank=True, max_length=50, null=True)),
                ('Office_State', models.CharField(blank=True, max_length=50, null=True)),
                ('Office_Country', models.CharField(blank=True, max_length=50, null=True)),
                ('Office_Pincode', models.IntegerField(blank=True, null=True)),
                ('Mode_of_Transpotation', models.CharField(blank=True, choices=[('College bus', 'College bus'), ('Own vehicle', 'Own vehicle'), ('By walk', 'By walk')], max_length=50, null=True)),
                ('Emergency_contact', models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Spouse', 'Spouse')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('Admission_number', models.IntegerField(blank=True, null=True)),
                ('Admission_date', models.DateField(blank=True, null=True)),
                ('Batch_name', models.CharField(blank=True, max_length=20, null=True)),
                ('Register', models.IntegerField(blank=True, null=True)),
                ('Roll_no', models.IntegerField(blank=True, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10, null=True)),
                ('Blood_group', models.CharField(blank=True, max_length=5, null=True)),
                ('Department', models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], max_length=200, null=True)),
                ('year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default='First', max_length=200, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('Aadhaar_no', models.IntegerField(blank=True, null=True)),
                ('Father_name', models.CharField(blank=True, max_length=200)),
                ('Father_phone', models.IntegerField(blank=True, null=True)),
                ('Occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('Mother_name', models.CharField(blank=True, max_length=200)),
                ('Mother_phone', models.IntegerField(blank=True, null=True)),
                ('Mother_Occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('Annual_income', models.IntegerField(blank=True, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=10, null=True)),
                ('Religion', models.CharField(blank=True, max_length=30, null=True)),
                ('Student_category', models.CharField(blank=True, choices=[('OC', 'OC'), ('BC', 'BC'), ('MBC', 'MBC'), ('SC\\ST', 'SC\\ST'), ('Other', 'Other')], max_length=10, null=True)),
                ('Door_no', models.IntegerField(blank=True, null=True)),
                ('Street_and_Area', models.CharField(blank=True, max_length=200, null=True)),
                ('District', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.CharField(blank=True, max_length=50, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Mode_of_Transpotation', models.CharField(blank=True, choices=[('College bus', 'College bus'), ('Own vehicle', 'Own vehicle'), ('By walk', 'By walk')], max_length=50, null=True)),
                ('Bus_route_no', models.IntegerField(blank=True, null=True)),
                ('Rugular_Boarding_point', models.CharField(blank=True, max_length=50, null=True)),
                ('Regular_dropping_point', models.CharField(blank=True, max_length=50, null=True)),
                ('Guardian_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Guardian_is', models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=20, null=True)),
                ('Guardian_mobile', models.IntegerField(blank=True, null=True)),
                ('Guardian_Address', models.CharField(blank=True, max_length=300, null=True)),
                ('Guardian_2_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Guardian_2_is', models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=20, null=True)),
                ('Guardian_2_mobile', models.IntegerField(blank=True, null=True)),
                ('Guardian_2_Address', models.CharField(blank=True, max_length=300, null=True)),
                ('Emergency_contact', models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=100, null=True)),
                ('subject_name', models.CharField(max_length=50, null=True)),
                ('regulation', models.CharField(choices=[('2017 regulation', '2017 regulation'), ('2021 regulation', '2021 regulation')], max_length=100, null=True)),
                ('department', models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], default='CSE', max_length=100, null=True)),
                ('year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=100)),
                ('semester', models.CharField(choices=[('odd', 'Odd'), ('even', 'Even')], max_length=20)),
                ('staff', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.staff')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=50, null=True)),
                ('regulation', models.CharField(choices=[('2017 regulation', '2017 regulation'), ('2021 regulation', '2021 regulation')], max_length=100, null=True)),
                ('department', models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical and Electronic Engineering', 'EEE'), ('Mechanical Engineering', 'Mech'), ('Civil Engineering', 'Civil')], default='CSE', max_length=100, null=True)),
                ('year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=100, null=True)),
                ('semester', models.CharField(choices=[('First', 'First'), ('Second', 'Second')], max_length=20, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('period_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_1', to='main.subject')),
                ('period_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_2', to='main.subject')),
                ('period_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_3', to='main.subject')),
                ('period_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_4', to='main.subject')),
                ('period_5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_5', to='main.subject')),
                ('period_6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_6', to='main.subject')),
                ('period_7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_7', to='main.subject')),
                ('period_8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period_8', to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('period_1', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p1reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_2', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p2reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_3', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p3reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_4', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p4reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_5', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p5reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_6', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p6reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_7', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p7reason', models.CharField(blank=True, max_length=500, null=True)),
                ('period_8', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('p8reason', models.CharField(blank=True, max_length=500, null=True)),
                ('reason', models.CharField(blank=True, max_length=500, null=True)),
                ('mark_attendance', models.CharField(blank=True, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
