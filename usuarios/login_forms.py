from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm  # Optional (built-in form)
from django import forms

class LoginForm(forms.Form):  # Use AuthenticationForm for built-in functionality
    username = forms.EmailField(
        label="Email",
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite seu Email"
            }
        )
    )
    password = forms.CharField(
        label="Senha de acesso",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite sua senha"
            }
        )
    )