from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name ="carrito"),
    path('', views.index_productos, name = "index_productos"),
    #en carrito.py funcion agregar esta el producto id. el agregar producto dle views, esta en el views
    path('agregar/<int:producto_id>/', views.agregar_producto, name = "agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name = "eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name = "restar"),
    # aciar no requiere producto_id, ya que elimina todos
    path('vaciar/', views.vaciar_carrito, name = "vaciar"),
    path('categorias/<int:categoria_id>/',views.categoria, name = "categoria_producto"),
    path('buscar/', views.buscar, name='busqueda_producto'),
    path('nuevo_producto/', views.nuevo_producto, name = 'nuevo_producto'),
    path('<int:pk>/', views.detalle_producto, name = 'detalle_producto'),
    path('<int:pk>/editar/', views.editar_producto, name = 'editar_producto'),
]