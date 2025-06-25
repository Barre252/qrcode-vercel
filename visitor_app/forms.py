from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser, VisitorRegistration
from django.forms.widgets import PasswordInput, TextInput

from django import forms


# Login Form
class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())


# Visitors registration form
class VisitorsForm(forms.ModelForm):
        class Meta:
                model = VisitorRegistration
                fields = '__all__'

