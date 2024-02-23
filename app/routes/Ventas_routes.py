from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Ventas import Ventas
from app.models.DetalleVentas import DetalleVentas
from app.routes.Carrito_routes import carrito_ventas
from app import db

bp = Blueprint('Ventas', __name__)

@bp.route('/Ventas')
def index():
    data = Ventas.query.all()
    # Ventas_list = [Ventas.to_dict() for book in data]
    # return jsonify(Ventas_list)
    return render_template('Ventas/index.html', data=data)

@bp.route('/Ventas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaVentas = request.form['fechaVentas']
        cantidadVentas = request.form['cantidadVentas']
        idClientes = request.form['idClientes']
        idEmpleados = request.form['idEmpleados']

        new_Ventas = Ventas(fechaVentas=fechaVentas, cantidadVentas=cantidadVentas, idClientes=idClientes, idEmpleados=idEmpleados)
        db.session.add(new_Ventas)
        db.session.commit()
        
        return redirect(url_for('Ventas.index'))

    return render_template('Ventas/add.html')
@bp.route('/adddetalleVenta/<int:id>', methods=['GET', 'POST'])  
def addDetalle(id):  
    for item in carrito_ventas.getItems():
        idproducto = item["producto"].idproducto        
        detalleventa = DetallesVentas(idventas=id,idproducto=idproducto)
        db.session.add(detalleventa)
        db.session.commit() 
    carrito_ventas.vaciarcarrito()
    return redirect(url_for('producto.index'))

@bp.route('/Ventas/edit/<int:idVentas>', methods=['GET', 'POST'])
def edit(idVentas):
    venta = Ventas.query.get_or_404(idVentas)

    if request.method == 'POST':
        venta.fechaVentas = request.form['fechaVentas']
        venta.cantidadVentas = request.form['cantidadVentas']
        venta.idClientes = request.form['idClientes']
        venta.idEmpleados = request.form['idEmpleados']

        db.session.commit()
        return redirect(url_for('Ventas.index'))

    return render_template('Ventas/edit.html', venta=venta)
    

@bp.route('/Ventas/delete/<int:idVentas>')
def delete(idVentas):
    ventas = Ventas.query.get_or_404(idVentas)
    
    db.session.delete(ventas)
    db.session.commit()

    return redirect(url_for('Ventas.index'))
