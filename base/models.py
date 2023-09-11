from django.db import models
from django.contrib.auth.models import AbstractUser




#Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Ticket(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #status =
    #category =
    responders = models.ManyToManyField(User, related_name='responders', blank=True)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tickets')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='submitted_tickets')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #priority
    
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return str(self.subject)
    
    

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-updated', '-created']
   
    def __str__(self):
        return self.body[0:20]   