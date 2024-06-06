from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .login_forms import LoginForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly created user
            return redirect('/')  # Redirect to home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            username = email.split('@')[0] 
            print(username)
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to home page after login
            else:
                # Handle invalid login credentials (optional)
                form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
                # You can also display an error message to the user
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})