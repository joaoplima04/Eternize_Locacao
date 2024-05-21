from django import forms
from categorias.models import Cliente
from django.contrib.auth.hashers import make_password  # For password hashing

class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite seu Email"
            }
        )
    )
    nome = forms.CharField(
        label="Nome completo",
         max_length=100,
          required=True,
          widget=forms.TextInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite seu nome completo"
            }
        )
    )
    cpf = forms.CharField(
        label="CPF",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite seu CPF"
            }
        )
    )
    telefone = forms.CharField(
        label="Telefone",
         max_length=20,
          required=True,
          widget=forms.TextInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite seu telefone"
            }
        )
    )
    data_nascimento = forms.DateField(
        label="Data Nascimento",
         required=True,
         widget=forms.DateInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite sua data de nascimento"
            }
        )
         )
    senha = forms.CharField(
        label="Senha de acesso",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Digite sua senha"
            }
        )
    )
    confirmar_senha = forms.CharField(
        label="Confirmação de senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Confirme sua senha"
            }
        )
    )

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não coincidem.')
        return confirmar_senha

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        # No need to create a User instance since we're using Cliente
        cliente = Cliente(
            email=self.cleaned_data['email'],
            nome=self.cleaned_data['nome'],
            cpf=self.cleaned_data['cpf'],
            telefone=self.cleaned_data['telefone'],
            data_nascimento=self.cleaned_data['data_nascimento'],
            username = email.split('@')[0],
            senha=make_password(self.cleaned_data['senha']),  # Hash password before saving
        )
        if commit:
            cliente.save()
        return cliente