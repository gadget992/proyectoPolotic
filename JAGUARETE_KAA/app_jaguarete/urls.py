
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name ="registro"),
    path('index/', views.index, name="inicio"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('registroInvalido/', views.registro_invalido, name = "registro_no_valido"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('contacto/', views.contacto, name="contacto"),
    
]