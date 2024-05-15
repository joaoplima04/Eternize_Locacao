from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm  # Optional (built-in form)
from django import forms

class LoginForm(AuthenticationForm):  # Use AuthenticationForm for built-in functionality
    username = forms.CharField(label="Email", max_length=255)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)