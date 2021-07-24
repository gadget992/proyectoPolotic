from .models import Categoria, Producto



#variable global en la que queremos que se vayan sumando los articulos del carro
def importe_total_carrito(request):
    
    total = 0

     #ver si el usuario esta autenticado, cuando lo probe no andaba porque nunca hicimos autenticacion
    #if request.user.is_authenticated:
    for key, value in request.session["carrito"].items():
        total = total + (float(value["precio"]))
    
    return {"importe_total_carrito" : total}



