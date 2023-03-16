from django.shortcuts import render
from .models import *

def frontpage(request):
    return render(request, 'base.html')

def timetable(request):
    print("hi")
    tt = TimeTable.objects.all()
    context = {"timetable":{"day":"Mon","period_1":"CD"}}
    return render(request,'admin/tt_change_list.html',context)