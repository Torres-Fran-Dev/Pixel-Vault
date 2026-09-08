from os import name
from django.urls import path
from .views import index,contacto
from home import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
]