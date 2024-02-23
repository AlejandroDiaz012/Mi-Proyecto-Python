from app.models.Productos import Productos

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto_id, cantidad):
        producto = Productos.query.get(producto_id)
        if producto:
            item = {'producto': producto, 'cantidad': cantidad}
            self.carrito.append(item)

    def calcular_total(self):
        return sum(item['producto'].precioProductos * item['cantidad'] for item in self.carrito)
    
    def tamañoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def vaciarcarrito(self):
        self.carrito = []