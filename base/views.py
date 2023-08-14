from django.shortcuts import render, redirect
from .models import Ticket
from .models import Message
from .forms import TicketForm

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
    tickets= Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'base/userdashboard.html', context)

def agentdashboard(request):
    tickets= Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'base/agentdashboard.html', context)

def admindashboard(request):
    tickets= Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'base/admindashboard.html', context)

def ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    context = {'ticket': ticket}        
    return render(request, 'base/ticket.html', context)

def createTicket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserDashboard')
    context ={'form' : form}
    return render(request, 'base/ticket_form.html', context)

def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('AgentDashboard')
    
    context ={'form' : form}
    return render(request, 'base/ticket_form.html', context)

def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect ('AdminDashboard')
    return render(request, 'base/delete.html', {'obj':ticket})