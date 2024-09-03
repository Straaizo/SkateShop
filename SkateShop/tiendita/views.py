from django.shortcuts import render,redirect
from .forms import Registro,FormularioEntrar
from django.contrib.auth.forms import UserCreationForm
from sweetify import info, success, warning, error
from django.contrib.auth import authenticate, login, logout

def mostrar_principal(request):
    return render(request,'pagina_principal.html')


