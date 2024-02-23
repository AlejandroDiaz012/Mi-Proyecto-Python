from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Compras import Compras
from app import db

bp = Blueprint('Compras', __name__)

@bp.route('/Compras')
def index():
    data = Compras.query.all()
    # Compras_list = [Compras.to_dict() for book in data]
    # return jsonify(Compras_list)
    return render_template('Compras/index.html', data=data)

@bp.route('/Compras/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaCompras = request.form['fechaCompras']
        cantidadCompras = request.form['cantidadCompras']
        idProveedores = request.form['idProveedores']
        idEmpleados = request.form['idEmpleados']

        new_Compras = Compras(fechaCompras=fechaCompras, cantidadCompras=cantidadCompras, idProveedores=idProveedores, idEmpleados=idEmpleados)
        db.session.add(new_Compras)
        db.session.commit()
        
        return redirect(url_for('Compras.index'))

    return render_template('Compras/add.html')

@bp.route('/Compras/edit/<int:idCompras>', methods=['GET', 'POST'])
def edit(idCompras):
    compra = Compras.query.get_or_404(idCompras)

    if request.method == 'POST':
        compra.fechaCompra = request.form['fechaCompras']
        compra.cantidadCompras = request.form['cantidadCompras']
        compra.idProveedores = request.form['idProveedores']
        compra.idEmpleados = request.form['idEmpleados']

        db.session.commit()
        return redirect(url_for('Compras.index'))

    return render_template('Compras/edit.html', compra=compra)
    

@bp.route('/Compras/delete/<int:idCompras>')
def delete(idCompras):
    compras = Compras.query.get_or_404(idCompras)
    
    db.session.delete(compras)
    db.session.commit()

    return redirect(url_for('Compras.index'))
