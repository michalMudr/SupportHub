from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="SupportHub"),
    path('userdashboard/', views.userdashboard, name="UserDashboard"),   
    path('agentdashboard/', views.agentdashboard, name="AgentDashboard"), 
    path('admindashboard/', views.admindashboard, name="AdminDashboard"),   
    path('ticket/<str:pk>/', views.ticket, name="ticket"),   
]

    

