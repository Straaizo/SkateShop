from django.urls import path
from .views import (
   mostrar_ruedas,mostrar_tablas,mostrar_trucks,mostrar_carrito,imagen_json
)
urlpatterns = [  path('tablas/',mostrar_tablas,name="pagina_tablas"),
    path('ruedas/',mostrar_ruedas,name="pagina_ruedas"),
    path('trucks/',mostrar_trucks,name="pagina_trucks"),
    path('carrito/',mostrar_carrito,name="pagina_carrito"),
   path('producto/<int:producto_id>/imagen/json/', imagen_json, name='imagen_json'),]
