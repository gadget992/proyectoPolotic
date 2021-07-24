from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .carrito import Carrito



# Create your views here.

#--------------PRODUCTOS EN LA PANTALLA PRINCIPAL
def index_productos(request):
    #le decimos que nos guarde en una variable todos los atributos de servicio, de la clase
    #no olvidar el tercer parametro, es para que cargue lo que guardamos
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    #recordar que el segundo parametro, el directorio arranca desde template
    return render(request, "productos/productos.html", {"productos" : productos, "categorias": categorias})

#-------------CARRITO Y SUS FUNCIONES---------

def carrito(request):
    #le decimos que nos guarde en una variable todos los atributos de servicio, de la clase
    #no olvidar el tercer parametro, es para que cargue lo que guardamos
    productos = Producto.objects.all()
    #recordar que el segundo parametro, el directorio arranca desde template
    return render(request, "productos/carrito.html", {"productos" : productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    #obtener el producto
    producto = Producto.objects.get(id = producto_id)

    #esta funcion es de la clase de carrito.py
    carrito.agregar(producto = producto)

    return redirect("carrito") 

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    #obtener el producto
    producto = Producto.objects.get(id = producto_id)

#     #esta funcion es de la clase de carrito.py
    carrito.eliminar(producto = producto)

    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    #obtener el producto
    producto = Producto.objects.get(id = producto_id)

    #esta funcion es de la clase de carrito.py
    carrito.restar_producto(producto = producto)

    return redirect("carrito")  

def vaciar_carrito(request, producto_id):
    carrito = Carrito(request)
    #obtener el producto
    producto = Producto.objects.get(id = producto_id)

    #este vaciar carrito es funcion del carrito.py
    carrito.vaciar_carrito()

    return redirect("carrito")

#-------------------------CATEGORIA--------------------
def categoria(request, categoria_id):

    categoria = Categoria.objects.only('titulo')
    #para que me muestre los posts relacionados con la cateroria
    # formCat = ProductoForm
    productos = Producto.objects.filter(categoria_id=categoria.id)
    return render(request, "productos/categorias.html", {"categoria" : categoria, "productos": productos})#, "formCat":formCat})


#----------------------BUSQUEDA PRODUCTOS-------------------

def buscar(request):

    if request.GET["texto_busqueda"]:

        producto_almacenado = request.GET["texto_busqueda"]
        
        if len(producto_almacenado)>20:
            mensaje = "texto introducido demasiado largo"
        
        else:
            
            producto = Producto.objects.filter(titulo__icontains = producto_almacenado)
            descripcion = Producto.objects.filter(descripcion__icontains = producto_almacenado)
            #me va a renderizar un html con el resultado de la busqueda
            #en el query se almacena el resultado de la busqueda por el usuario
            #el articulo chequea si esta en la BBDD
            
            return render(request, "productos/resultado_busqueda.html", {"producto":producto,
            "query":producto_almacenado, "descripcion": descripcion})
        
    else:
        mensaje = "no escribiste nada"

    return HttpResponse(mensaje)


#-----------------------NUEVO PRODUCTO-----------------------

def nuevo_producto(request):
    


    if request.method =='POST':
        
        form = ProductoForm(request.POST, request.FILES)
        
        if form.is_valid():
            producto = form.save()
            
            return redirect('detalle_producto', pk=producto.pk)
            
        else:
            
            return HttpResponse("chau")

    else:
        
        form = ProductoForm
        return render(request, 'productos/nuevo_producto.html', {'form': form})




def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto':producto})


def editar_producto(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    print("hola1")
    if request.method == 'POST':
        print("entro al if")        
        form = ProductoForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            print("formulario coRRecto")
            producto = form.save()
            return redirect('detalle_producto', pk=pk)


    else:
        print("entro al else")
        form = ProductoForm(instance=producto)
    
    print("hola2")
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto':producto})


