from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .forms import FormularioEntrar, Registro
from sweetify import info, success, warning, error
# Create your views here.
def mostrar_registrar(request):
    if request.method == 'GET':
        contexto = {
            'formulario' : Registro()
        }
        return render(request,'pagina_registrarse.html',contexto)
    if request.method == 'POST':
        formulario_registro = Registro(data=request.POST)
        es_valido = formulario_registro.is_valid() # Retorna un bool
        if es_valido: # Si bool es True
            usuario_nuevo = formulario_registro.save()
            success(request,'Gracias por Unirte :)')
            return redirect('pagina_principal')
        contexto = {
            'formulario': formulario_registro
        }
        warning(request,'Ups... Observer los campos con errores y vuelva a intentarlo...')
        return render(request,'pagina_registrarse.html',contexto)    
    
def mostrar_login(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':FormularioEntrar(), 
        }
        return render(request,'pagina_login.html',contexto)
    if request.method == 'POST':
        datos_usuario = FormularioEntrar(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username =  datos_usuario.cleaned_data['usuario'],
                password = datos_usuario.cleaned_data['contrasenia_usuario']
            )   #Login
            if usuario is not None:
                login(request, usuario)
                success(request,f'Bienvenido {usuario.first_name}')
                return redirect('pagina_principal')
        warning(request,'Usuario y contraseña invalidos :( ')       
        contexto = {
            'formulario' : datos_usuario
        }
        return render(request,'pagina_login.html',contexto)  


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request,'Sesion Cerrada.')
    return redirect('pagina_principal')    