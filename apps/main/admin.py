from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import Widget


class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff


class StaffAdmin(ImportExportModelAdmin):
    resource_classes = [StaffResource]


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin):
    resource_classes = [StudentResource]


class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['department', 'year', 'semester']
    list_display = ['subject_code', 'subject_name',
                    'staff', 'department', 'year', 'semester']


class TimeTableAdmin(admin.ModelAdmin):
    change_list_template = 'admin/timetable_change_list.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        values = False
        if request.method == 'POST':
            dept = request.POST.get('department')
            year = request.POST.get('year')
            values = True
            if dept == 'CSE':
                dept = 'Computer Science and Engineering'
            elif dept == 'ECE':
                dept = 'Electronics and Communication Engineering'
            elif dept == 'EEE':
                dept = 'Electrical and Electronic Engineering'
            elif dept == 'Mech':
                dept = 'Mechanical Engineering'
            elif dept == 'Civil':
                dept = 'Civil Engineering'
            monday = TimeTable.objects.filter(
                day="Monday", subject_name__department=dept, subject_name__year=year)
            tuesday = TimeTable.objects.filter(
                day="Tuesday", subject_name__department=dept, subject_name__year=year)
            wednesday = TimeTable.objects.filter(
                day="Wednesday", subject_name__department=dept, subject_name__year=year)
            thursday = TimeTable.objects.filter(
                day="Thursday", subject_name__department=dept, subject_name__year=year)
            friday = TimeTable.objects.filter(
                day="Friday", subject_name__department=dept, subject_name__year=year)
            sub = Subject.objects.filter(department=dept, year=year)
            extra_context.update({
                "monday": monday,
                'tuesday': tuesday,
                'wednesday': wednesday,
                'thursday': thursday,
                'friday': friday,
                'sub': sub,
                'values': values
            })

            return super().changelist_view(request, extra_context=extra_context)
        else:
            return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
