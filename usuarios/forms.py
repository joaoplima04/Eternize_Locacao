from django import forms
from categorias.models import Cliente
from django.contrib.auth.hashers import make_password  # For password hashing

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    nome = forms.CharField(label="Nome completo", max_length=100, required=True)
    cpf = forms.CharField(label="CPF", max_length=100, required=True)
    telefone = forms.CharField(label="Telefone", max_length=20, required=True)
    data_nascimento = forms.DateField(label="Data Nascimento", required=True)
    senha = forms.CharField(label="Senha de acesso", widget=forms.PasswordInput, required=True)
    confirmar_senha = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput, required=True)

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não coincidem.')
        return confirmar_senha

    def save(self, commit=True):
        # No need to create a User instance since we're using Cliente
        cliente = Cliente(
            email=self.cleaned_data['email'],
            nome=self.cleaned_data['nome'],
            cpf=self.cleaned_data['cpf'],
            telefone=self.cleaned_data['telefone'],
            data_nascimento=self.cleaned_data['telefone'],
            password=make_password(self.cleaned_data['senha']),  # Hash password before saving
        )
        if commit:
            cliente.save()
        return cliente