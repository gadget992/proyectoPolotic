class Carrito:

    #aca creamos la sesion con un constructor
    def __init__(self, request):
        self.request = request
        self.session = request.session
        #aca almacenamos la variable carrito, que inicia session
        
        carrito = self.session.get("carrito")
        #aca si el usuario no tiene carrito, crea una session. El carrito es un diccionario
        if not carrito:
            carrito = self.session['carrito'] = {}
        #si ya hay carrito, que siga siendo el que estaba antes
        #esto me daba error, asi que comente el else y el self.carrito esta sin indentar
        #else:
        self.carrito = carrito
        

    #agregar productos al carrito. Si el ID del producto no esta en carrito, lo agregamos
    #el self.carrito.keys es para obtener la clave (de dict clave valor) que le creamos.
    def agregar(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "producto_id" : producto.id,
                "titulo": producto.titulo,
                "precio" : str(producto.precio),
                "cantidad" : 1,
                #no olvidarse de poner url
                "imagen" : producto.imagen.url,
            }
        #si el producto.id esta en el carrito...recorrelo con el for. si la clave (de clave valor) es igual al id
        #, sumame la cantidad en 1 del producto. Es decir recorre toda la lista de productos y si encuentra coincidencias
        #en el id, me lo suma al producto. despues el break para que no me recorra la lista si hay 100 productos,
        #cuando encuentre un id, no hace falta recorrer mas
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        #actualiza el carrito cuando hay cambios, esta la funcion abajo
        self.guardar_carrito()
  
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
     #eliminar un producto, este elimina el producto del todo, despues esta la de restar
    def eliminar(self, producto):
        producto.id = str(producto.id)
        #evaluamos primero si el producto esta en el carrito, si esta lo borramos. por ultimo actualizamos de nuevo el carrito
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()
    
    #borrar productos
    def restar_producto(self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] - 1
                    value["precio"] = float(value["precio"])-producto.precio
                    #si tengo en mi carrito 1 producto, le resto otro me queda 0, hay que eliminar el producto del carrito
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                   
                    break

        #actualiza el carrito cuando hay cambios, esta la funcion abajo
        self.guardar_carrito()

    #vaciar carrito. lo limpiamos
    def vaciar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True

