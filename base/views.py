from django.shortcuts import render
from django.http import HttpResponse

# Create your views

def home(request):
    return HttpResponse('Home Page')
def userdashboard(request):
    return HttpResponse('User Dashboard')
