from django.db import models


year_choices = [
    ('First', 'First'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
]

dept_choices = [
    ('Computer Science and Engineering', 'CSE'),
    ('Electronics and Communication Engineering', 'ECE'),
    ('Electrical and Electronic Engineering', 'EEE'),
    ('Mechanical Engineering', 'Mech'),
    ('Civil Engineering', 'Civil')
]
gender_choices = [
    ('Male', 'male'),
    ('Female', 'female')
]

category_choices = [
    ('OC', 'OC'),
    ('BC', 'BC'),
    ('MBC', 'MBC'),
    ('SC\ST', 'SC\ST'),
    ('Other', 'Other')
]
guardian_choice = [
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Local Guardian', 'Local Guardian'),
    ('Local Guardian 2', 'Local Guardian 2')
]
transport_choice = [
    ('College bus', 'College bus'),
    ('Own vehicle', 'Own vehicle'),
    ('By walk', 'By walk')
]


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    Admission_number = models.IntegerField(null=True, blank=True)
    Admission_date = models.DateField(null=True, blank=True)
    Batch_name = models.CharField(max_length=20, null=True, blank=True)
    Register = models.IntegerField(null=True, blank=True)
    Roll_no = models.IntegerField(null=True, blank=True)
    Age = models.IntegerField(null=True)
    DOB = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=gender_choices, null=True)
    Blood_group = models.CharField(max_length=5, null=True, blank=True)
    Department = models.CharField(max_length=200, choices=dept_choices)
    year = models.CharField(
        max_length=200, default='First', choices=year_choices, null=True)
    Phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    Aadhaar_no = models.IntegerField(null=True, blank=True)
    Father_name = models.CharField(max_length=200, blank=True)
    Father_phone = models.IntegerField(null=True, blank=True)
    Occupation = models.CharField(max_length=50, null=True, blank=True)
    Mother_name = models.CharField(max_length=200, blank=True)
    Mother_phone = models.IntegerField(null=True, blank=True)
    Mother_Occupation = models.CharField(max_length=50, null=True, blank=True)
    Annual_income = models.IntegerField(null=True, blank=True)
    Nationality = models.CharField(max_length=10, null=True, blank=True)
    Religion = models.CharField(max_length=30, null=True, blank=True)
    Student_category = models.CharField(
        max_length=10, choices=category_choices, null=True, blank=True)
    Door_no = models.IntegerField(null=True, blank=True)
    Street_and_Area = models.CharField(max_length=200, null=True, blank=True)
    District = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Mode_of_Transpotation = models.CharField(
        max_length=50, choices=transport_choice, null=True, blank=True)
    Bus_route_no = models.IntegerField(null=True, blank=True)
    Rugular_Boarding_point = models.CharField(
        max_length=50, null=True, blank=True)
    Regular_dropping_point = models.CharField(
        max_length=50, null=True, blank=True)
    Guardian_name = models.CharField(max_length=50, null=True, blank=True)
    Guardian_is = models.CharField(
        max_length=20, choices=guardian_choice, null=True, blank=True)
    Guardian_mobile = models.IntegerField(null=True, blank=True)
    Guardian_Address = models.CharField(max_length=300, null=True, blank=True)
    Guardian_2_name = models.CharField(max_length=50, null=True, blank=True)
    Guardian_2_is = models.CharField(
        max_length=20, choices=guardian_choice, null=True, blank=True)
    Guardian_2_mobile = models.IntegerField(null=True, blank=True)
    Guardian_2_Address = models.CharField(
        max_length=300, null=True, blank=True)
    Emergency_contact = models.CharField(
        max_length=30, choices=guardian_choice, null=True, blank=True)

    def __str__(self):
        return self.name


employee_choice = [
    ('Assistant professor', 'Assistant professor'),
    ('Professor', 'Professor'),
    ('Lab Staff', 'Lab Staff'),
    ('Supporting Staff', 'Supporting Staff'),
    ('Driver', 'Driver'),
    ('Maintenance Staff', 'Maintenance Staff')
]
marital_choice = [
    ('Single', 'Single'),
    ('Married', 'Married')
]
Emergency_choice = [
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Spouse', 'Spouse')
]


class Staff(models.Model):
    Employee_ID = models.CharField(max_length=5, null=True)
    Employee_Category = models.CharField(
        max_length=30, choices=employee_choice, null=True)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, null=True)
    Father_name = models.CharField(max_length=50, null=True)
    Mother_name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200)
    Home_contact_No = models.IntegerField(null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=10, choices=gender_choices, null=True)
    Blood_group = models.CharField(max_length=10, null=True)
    Aadhaar_no = models.IntegerField(null=True)
    DOB = models.DateField(null=True)
    Date_of_Joining = models.DateField(null=True)
    Marital_Status = models.CharField(
        max_length=10, choices=marital_choice, null=True)
    Spouse_Name = models.CharField(max_length=30, null=True)
    Children_count = models.IntegerField(null=True)
    Department = models.CharField(max_length=200, choices=dept_choices)
    Qualification = models.CharField(max_length=50, null=True)
    Experience = models.CharField(max_length=50, null=True)
    Religion = models.CharField(max_length=30, null=True)
    Community = models.CharField(
        max_length=10, choices=category_choices, null=True)
    Door_no = models.IntegerField(null=True)
    Street_and_Area = models.CharField(max_length=200, null=True)
    District = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    Pincode = models.IntegerField(null=True)
    Office_Door_no = models.IntegerField(null=True)
    Office_Street_and_Area = models.CharField(max_length=200, null=True)
    Office_District = models.CharField(max_length=50, null=True)
    Office_State = models.CharField(max_length=50, null=True)
    Office_Country = models.CharField(max_length=50, null=True)
    Office_Pincode = models.IntegerField(null=True)
    Mode_of_Transpotation = models.CharField(
        max_length=50, choices=transport_choice, null=True)
    Emergency_contact = models.CharField(
        max_length=30, choices=Emergency_choice, null=True)

    def __str__(self):
        return self.name


regulation_choices = [
    ('2017 regulation', '2017 regulation'),
    ('2021 regulation', '2021 regulation')
]

sem_choices = [
    ('First', 'First'),
    ('Second', 'Second'),
]


class Subject(models.Model):
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=500)
    department = models.CharField(
        max_length=200, default='CSE', choices=dept_choices)
    year = models.CharField(
        max_length=200, default='First', choices=year_choices)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    regulation = models.CharField(
        max_length=100, default='2017 regulation', choices=regulation_choices)
    semester = models.CharField(
        max_length=100, default='First', choices=sem_choices)

    def __str__(self):
        return self.subject_name


day_choice = [
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday")
]

period_choice = [
    ('First', 'First'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
    ('Fifth', 'Fifth'),
    ('Sixth', 'Sixth'),
    ('Seventh', 'Seventh'),
    ('Eight', 'Eight'),

]


class TimeTable(models.Model):
    day = models.CharField(max_length=100, null=True, choices=day_choice)
    period = models.CharField(max_length=50, null=True, choices=period_choice)
    subject_name = models.ForeignKey(
        Subject, null=True, related_name='subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.day+' '+self.period+' '+' period'


att_choice = [
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('On Duty', 'On Duty')
]


class StudentAttendance(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, null=True, choices=day_choice)
    date = models.DateField()
    time = models.TimeField()
    period_1 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_2 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_3 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_4 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_5 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_6 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_7 = models.CharField(max_length=100, choices=att_choice, null=True)
    period_8 = models.CharField(max_length=100, choices=att_choice, null=True)
    reason = models.CharField(max_length=500, null=True, blank=True)
    mark_attendance = models.CharField(max_length=100, choices=att_choice)
