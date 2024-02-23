from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Productos import Productos
from app.models.Carrito import Carrito
from app.models.Ventas import Ventas
from app.models.DetalleVentas import DetalleVentas
from flask_login import current_user
from app import db

bp = Blueprint('carritos', __name__)
carrito_ventas = Carrito()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_ventas.getItems()
    return render_template('Productos/List.html', items=items)

@bp.route('/ListarProductos')
def index():
    productos = carrito_ventas
    return render_template('index.html', productos=productos)

@bp.route('/agregar/<int:id>', methods=['POST'])
def agregar_al_carrito(id):
    cantidad = int(request.form.get('cantidad', 1))
    carrito_ventas.agregar_producto(id, cantidad)
    
    return redirect(url_for
    
    ('Productos1.index'))
    #return "Entra a agregar corrito"

@bp.route('/realizar_compra')
def realizar_compra():
    total = carrito_ventas.calcular_total()
    suma = carrito_ventas.tamañoD()
    
    new_venta = Ventas(cantidadVentas=suma,idClientes=current_user.idClientes, total=total)
    db.session.add(new_venta)
    db.session.commit()

    factura = carrito_ventas.getItems()

    for producto in factura:

        
        producto2 = producto['producto']
        detalles = DetalleVentas(cantidadDetalle=producto['cantidad'], subTotalDetalle=producto2.precioProductos, idVentas=new_venta.idVentas, idProductos=producto2.idProductos)
        db.session.add(detalles)

    db.session.commit()
    detalle = DetalleVentas.query.filter_by(idVentas=new_venta.idVentas).all()

    return render_template('Carrito/realizar_Compra.html', detalles=detalle,new_venta=new_venta)

@bp.route('/generar_factura', methods=['POST'])
def generar_factura():
    total = carrito_ventas.calcular_total()
   
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carrito_ventas.carrito = []
    return render_template('Carrito/venta.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carrito_ventas.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_ventas.tamañoD()}"



