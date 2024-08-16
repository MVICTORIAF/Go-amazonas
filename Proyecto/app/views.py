from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ProfileForm
from .models import Profile

# Vistas básicas

def inicio(request):
    return render(request, 'app/index.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

def destinos(request):
    return render(request, 'app/destinos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

# Vistas para autenticación y manejo de perfiles



# Vista para hacer login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirige a la página de perfil después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para editar el perfil del usuario
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la misma página después de guardar los cambios
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirige a la página de perfil después de registrarse
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

