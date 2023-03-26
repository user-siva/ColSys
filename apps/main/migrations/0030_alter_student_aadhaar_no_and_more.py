# Generated by Django 4.1.7 on 2023-03-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_studentattendance_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Aadhaar_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Admission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Admission_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Annual_income',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Batch_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Blood_group',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Bus_route_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='District',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Door_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Emergency_contact',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Father_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='Father_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_2_Address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_2_is',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_2_mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_2_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_Address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_is',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Local Guardian', 'Local Guardian'), ('Local Guardian 2', 'Local Guardian 2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mode_of_Transpotation',
            field=models.CharField(blank=True, choices=[('College bus', 'College bus'), ('Own vehicle', 'Own vehicle'), ('By walk', 'By walk')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mother_Occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mother_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mother_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Nationality',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Register',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Regular_dropping_point',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Religion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Rugular_Boarding_point',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='State',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Street_and_Area',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_category',
            field=models.CharField(blank=True, choices=[('OC', 'OC'), ('BC', 'BC'), ('MBC', 'MBC'), ('SC\\ST', 'SC\\ST'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
