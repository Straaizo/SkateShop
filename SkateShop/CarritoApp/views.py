
from django.shortcuts import render, redirect
from django.http import JsonResponse
from CarritoApp.models import Producto
from CarritoApp.Carrito import Carrito

# Create your views here.
def mostrar_tablas(request):
    productos = Producto.objects.filter(categoria='Tablas')
    return render(request,'pagina_tablas.html ',{'productos':productos})

def mostrar_carrito(request):
    return render(request,'carrito.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('pagina_carrito')

def eliminar_producto (request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('pagina_carrito')

def restar_producto (request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('pagina_carrito')

def limpiar_carrito(request):
    current_url = request.get_full_path()
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('pagina_carrito')
    

def mostrar_ruedas (request):
    productos = Producto.objects.filter(categoria='Ruedas')
    return render(request,'pagina_ruedas.html ',{'productos':productos})

def mostrar_trucks (request):
    productos = Producto.objects.filter(categoria='Trucks')
    return render(request,'pagina_trucks.html',{'productos':productos})

def imagen_json(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        data = {
            'imagen_url': producto.imagen_url(),  # Usa el método imagen_url para obtener la URL de la imagen
        }
        return JsonResponse(data)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)