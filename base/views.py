from django.shortcuts import render
from .models import Ticket
from .models import Message

# Create your views

#tickets = [
    #{'id':1, 'subject':'Can not login!'},
    #{'id':2, 'subject':'Order enquery!'},
    #{'id':3, 'subject':'Refund!'},
#]

def home(request):
    tickets= Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'base/home.html', context)

def userdashboard(request):
    return render(request, 'base/userdashboard.html')

def agentdashboard(request):
    return render(request, 'base/agentdashboard.html')

def admindashboard(request):
    return render(request, 'base/admindashboard.html')

def ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    context = {'ticket': ticket}        
    return render(request, 'base/ticket.html', context)
