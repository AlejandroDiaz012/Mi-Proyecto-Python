from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Productos import Productos
from app.routes.Carrito_routes import carrito_ventas
from app import db
import os


bp = Blueprint('Productos', __name__)

@bp.route('/Productos')
def index():
    data = Productos.query.all()
    # Productos_list = [Productos.to_dict() for book in data]
    # return jsonify(Productos_list)
    return render_template('Productos/index.html', data=data,t=carrito_ventas.tamañoD())

@bp.route('/Productos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreProductos = request.form['nombreProductos']
        descripcionProductos = request.form['descripcionProductos']
        precioProductos = request.form['precioProductos']
        fechaCaducidadProductos = request.form['fechaCaducidadProductos']
        Imagen = request.files['nombreImagen']

        new_Productos = Productos(nombreProductos=nombreProductos, descripcionProductos=descripcionProductos, precioProductos=precioProductos, fechaCaducidadProductos=fechaCaducidadProductos, nombreImagen=Imagen.filename)
        guardarImagen(Imagen)   
        db.session.add(new_Productos)
        db.session.commit()
        
        return redirect(url_for('Productos.index'))

    return render_template('Productos/add.html')

@bp.route('/Productos/edit/<int:idProductos>', methods=['GET', 'POST'])
def edit(idProductos):
    producto = Productos.query.get_or_404(idProductos)

    if request.method == 'POST':
        producto.nombreProductos = request.form['nombreProductos']
        producto.descripcionProductos = request.form['descripcionProductos']
        producto.precioProductos = request.form['precioProductos']
        producto.fechaCaducidadProductos = request.form['fechaCaducidadProductos']
        
        db.session.commit()
        return redirect(url_for('Productos.index'))

    return render_template('Productos/edit.html', producto=producto)
    

@bp.route('/Productos/delete/<int:idProductos>')
def delete(idProductos):
    productos = Productos.query.get_or_404(idProductos)
    
    db.session.delete(productos)
    db.session.commit()
    return redirect(url_for('Productos.index'))


def guardarImagen(imagen):
    from run import app
    carpetaDestino = os.path.join(app.root_path, "static", "imagenes")
    imagen.save(os.path.join(carpetaDestino, imagen.filename))


def eliminar(idProductos):
    from run import app
    producto = Productos.query.get_or_404(idProductos)
    ruta_imagen = os.path.join(app.root_path, "static", "imagenes", producto.nombreImagen)

    if os.path.exists(ruta_imagen):
        os.remove(ruta_imagen)
