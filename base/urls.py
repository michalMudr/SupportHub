from django.urls import path
from . import views



urlpatterns = [
    path ('login/', views.loginPage, name="login"),
    path ('logout/', views.logoutUser, name="logout"),
    path ('register/', views.registerPage, name="register"),
    
    path('', views.home, name="Home"),
    path('userdashboard/', views.userdashboard, name="UserDashboard"),   
    path('agentdashboard/', views.agentdashboard, name="AgentDashboard"), 
    path('admindashboard/', views.admindashboard, name="AdminDashboard"),   
    path('ticket/<str:pk>/', views.ticket, name="ticket"),   
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('create-ticket/', views.createTicket, name="create-ticket"),
    path('update-ticket/<str:pk>/', views.updateTicket, name="update-ticket"),
    path('delete-ticket/<str:pk>/', views.deleteTicket, name="delete-ticket"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    
    path('update-user/', views.updateUser, name="update-user"),
    
]

    

