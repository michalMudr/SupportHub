from django.db import models
from django.contrib.auth.models import User





# Create your models here.


class Ticket(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #status =
    #category =
    
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tickets')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='submitted_tickets')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #priority
    
    def __str__(self):
        return str(self.subject)
    
    

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:20]   