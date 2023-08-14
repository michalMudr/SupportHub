from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="Home"),
    path('userdashboard/', views.userdashboard, name="UserDashboard"),   
    path('agentdashboard/', views.agentdashboard, name="AgentDashboard"), 
    path('admindashboard/', views.admindashboard, name="AdminDashboard"),   
    path('ticket/<str:pk>/', views.ticket, name="ticket"),   
    
    path('create-ticket/', views.createTicket, name="create-ticket"),
    path('update-ticket/<str:pk>/', views.updateTicket, name="update-ticket"),
    path('delete-ticket/<str:pk>/', views.deleteTicket, name="delete-ticket"),
    
]

    

