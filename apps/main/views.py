from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse


def frontpage(request):
    return render(request, 'base.html')


def submitAttend(request):
    data = json.loads(request.body)
    for i in data:
        try:
            print(i)
            name = i["name"]
            stu = Student.objects.get(name=name)
            date = str(data[-1])
            StudentAttendance.objects.create(name=stu, date=date, period_1=i['period_1'], period_2=i['period_2'],
                                             period_3=i['period_3'], period_4=i['period_4'], period_5=i['period_5'],
                                             period_6=i['period_6'], period_7=i['period_7'], period_8=i['period_8'],
                                             reason=i['Reason'])
        except:
            pass
    return JsonResponse({'Success': True})
