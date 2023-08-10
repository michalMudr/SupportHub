from django.contrib import admin

# Register your models here.
from .models import Ticket, Message

admin.site.register(Ticket)
admin.site.register(Message)