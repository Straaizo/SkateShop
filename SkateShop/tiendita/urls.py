"""
URL configuration for tiendita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from .views import mostrar_principal
from CarritoApp.views import agregar_producto,eliminar_producto,restar_producto,limpiar_carrito


urlpatterns = [
    path('',mostrar_principal,name="pagina_principal"),
    path('',include('e_user.urls')),
    path('',include('CarritoApp.urls')),
    path('agregar/<int:producto_id>/',agregar_producto,name="Add"),
    path('eliminar/<int:producto_id>/',eliminar_producto,name="Del"),
    path('restar/<int:producto_id>/',restar_producto,name="Sub"),
    path('limpiar/',limpiar_carrito,name="CLS"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True : 
    urlpatterns+=static(settings.STATIC_URL, root_document=settings.STATIC_ROOT)

if settings.DEBUG == True : 
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)