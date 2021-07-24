from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == "POST":
        formulario = CustomUserForm(request.POST)

        while formulario.errors:
            return render(request, 'registration/registro_invalido.html', data)
        
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            
            return redirect('index_productos')
        # elif formulario.errors:
        #     return render(request, 'registration/registro_invalido.html', data)

    return render (request, "registration/registro.html", data)

def index(request):
    return render (request, 'app_jaguarete/index.html')

def registro_invalido(request):
    return render (request, 'registration/registro_invalido.html')

def acerca_de(request):
    return render(request, 'app_jaguarete/acerca_de.html')

def contacto(request):
    return render(request, 'app_jaguarete/contacto.html')

