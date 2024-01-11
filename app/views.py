from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.forms import *

def create_school(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('create_school done..')
        else:
            return HttpResponse('Invalid Data....')

    return render(request,'create_school.html',context=d)

