from django.forms import ModelForm
from .models import Ticket, User
from django.contrib.auth.forms import UserCreationForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['responders', 'user']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio' ]