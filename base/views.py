from django.shortcuts import render
from django.http import HttpResponse

# Create your views

tickets = [
    {'id':1, 'subject':'Can not login!'},
    {'id':2, 'subject':'Order enquery!'},
    {'id':3, 'subject':'Refund!'},
]

def home(request):
    context = {'tickets': tickets}
    return render(request, 'base/home.html', context)

def userdashboard(request):
    return render(request, 'base/userdashboard.html')

def agentdashboard(request):
    return render(request, 'base/agentdashboard.html')

def admindashboard(request):
    return render(request, 'base/admindashboard.html')

def ticket(request, pk):
    ticket = None
    for i in tickets:
        if i['id'] == int(pk):
            ticket = i
    context = {'ticket': ticket}        
    return render(request, 'base/ticket.html', context)
