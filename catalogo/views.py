from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Juego

def lista_juegos(request):
    query = request.GET.get('q', '')
    if query:
        juegos_list = Juego.objects.filter(nombre__icontains=query).order_by('nombre')
    else:
        juegos_list = Juego.objects.all().order_by('nombre')
    
    paginator = Paginator(juegos_list, 6) # Muestra 6 juegos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'catalogo/lista.html', {'page_obj': page_obj, 'query': query})

def detalle_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'catalogo/detalle.html', {'juego': juego})

def agregar_carrito(request, juego_id):
    carrito = request.session.get('carrito', {})
    id_str = str(juego_id)
    
    if id_str in carrito:
        carrito[id_str]['cantidad'] += 1
    else:
        juego = get_object_or_404(Juego, id=juego_id)
        carrito[id_str] = {
            'nombre': juego.nombre,
            'precio': float(juego.precio),
            'imagen': juego.imagen,
            'cantidad': 1
        }
        
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'catalogo/carrito.html', {'carrito': carrito, 'total': total})

def eliminar_del_carrito(request, juego_id):
    carrito = request.session.get('carrito', {})
    id_str = str(juego_id)
    
    if id_str in carrito:
        del carrito[id_str]
        request.session['carrito'] = carrito
        
    return redirect('ver_carrito')


def finalizar_compra(request):
    # Vaciamos el carrito eliminando la variable de la sesión
    if 'carrito' in request.session:
        del request.session['carrito']
    return render(request, 'catalogo/exito.html')