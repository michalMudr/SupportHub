from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Ticket, Message, User
from .forms import TicketForm, UserForm, MyUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('UserDashboard')
        else:
         messages.error(request, form.errors)
      
            
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tickets= Ticket.objects.filter(
        Q(subject__icontains=q) |
        Q(description__icontains=q) 
        )
    
    tickets= Ticket.objects.all()
    ticketmessages = Message.objects.filter(Q(ticket__subject__icontains=q))
    
    context = {'tickets': tickets, 'ticketmessages':ticketmessages }
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
    responders = ticket.responders.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            ticket=ticket,
            body=request.POST.get('body')
        )
        ticket.responders.add(request.user)
        return redirect('ticket', pk=ticket.id)
    
    context = {'ticket': ticket, 'ticketmessages': ticketmessages, 'responders': responders}        
    return render(request, 'base/ticket.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
   
    ticket = Ticket.objects.get(id=pk)
    ticketmessages = user.message_set.all()
    
    
    context = {'user':user, 'ticketmessages':ticketmessages }
    return render(request, 'base/profile.html', context)
    

@login_required(login_url='login')
def createTicket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('UserDashboard')
    context ={'form' : form}
    return render(request, 'base/ticket_form.html', context)

@login_required(login_url='login')
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    
    if request.user != ticket.user:
        return HttpResponse('You are not allowed to update ticket!!!')
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('UserDashboard')
    
    context ={'form' : form}
    return render(request, 'base/ticket_form.html', context)

@login_required(login_url='login')
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    
    if request.user != ticket.agent:
        return HttpResponse('You are not allowed to delete ticket!!!')
    
    if request.method == 'POST':
        ticket.delete()
        return redirect ('AdminDashboard')
    
    return render(request, 'base/delete.html', {'obj':ticket})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not allowed to delete message!!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect ('UserDashboard')
    
    return render(request, 'base/delete.html', {'obj':message})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
        
    return render(request, 'base/update-user.html', {'form': form})