from django.shortcuts import render
from django.http import HttpResponse

# Create your views

def home(request):
    return render(request, 'home.html')

def userdashboard(request):
    return render(request, 'userdashboard.html')
