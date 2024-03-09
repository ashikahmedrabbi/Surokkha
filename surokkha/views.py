from django.http import HttpResponse
from django.shortcuts import render
from doctor.models import Doctor


def home(request):
    doctors = Doctor.objects.all() 
    return render(request, 'home.html', {'doctors': doctors})
    