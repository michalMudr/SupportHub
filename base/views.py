from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Ticket
from .models import Message
from .forms import TicketForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views

#tickets = [
    #{'id':1, 'subject':'Can not login!'},
    #{'id':2, 'subject':'Order enquery!'},
    #{'id':3, 'subject':'Refund!'},
#]

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('UserDashboard')
        else:
            messages.error(request, 'Username OR password does not exist')
    
    context ={'page' : page }
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('UserDashboard')
        else:
            messages.error(request, ' An error occured during registration')
            
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tickets= Ticket.objects.filter(
        Q(subject__icontains=q) |
        Q(description__icontains=q) 
        )
    
    
    context = {'tickets': tickets, }
    return render(request, 'base/home.html', context)

def userdashboard(request):
   
    tickets= Ticket.objects.all()
    context = {'tickets': tickets, }
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
    ticketmessages = ticket.message_set.all().order_by('-created')
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            ticket=ticket,
            body=request.POST.get('body')
        )
        return redirect('ticket', pk=ticket.id)
    
    context = {'ticket': ticket, 'ticketmessages': ticketmessages}        
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