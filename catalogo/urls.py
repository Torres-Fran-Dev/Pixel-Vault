from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name='catalogo'),
    path('juego/<uuid:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('catalogo/', views.lista_juegos, name='lista_juegos'),
    path('carrito/agregar/<uuid:juego_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<uuid:juego_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/exito/', views.finalizar_compra, name='finalizar_compra'),
]