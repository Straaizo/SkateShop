from django.urls import path
from .views import (
   mostrar_registrar,mostrar_login,cerrar_sesion
)
urlpatterns = [ path('registrarse/',mostrar_registrar,name="pagina_registrarse"),
    path('entrar/',mostrar_login,name="pagina_entrar"),
    path('salir/',cerrar_sesion,name='cerrar_sesion'),]