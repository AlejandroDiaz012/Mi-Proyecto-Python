from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.DetalleCompras import DetalleCompras
from app import db

bp = Blueprint('DetalleCompras', __name__)

@bp.route('/DetalleCompras')
def index():
    data = DetalleCompras.query.all()
    # DetalleCompras_list = [DetalleCompras.to_dict() for book in data]
    # return jsonify(DetalleCompras_list)
    return render_template('DetalleCompras/index.html', data=data)

@bp.route('/DetalleCompras/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cantidadDetalle = request.form['cantidadDetalle']
        subTotalDetalle = request.form['subTotalDetalle']
        idProductos = request.form['idProductos']
        idCompras = request.form['idCompras']

        new_DetalleCompras = DetalleCompras(cantidadDetalle=cantidadDetalle, subTotalDetalle=subTotalDetalle, idProductos=idProductos, idCompras=idCompras)
        db.session.add(new_DetalleCompras)
        db.session.commit()
        
        return redirect(url_for('DetalleCompras.index'))

    return render_template('DetalleCompras/add.html')

@bp.route('/DetalleCompras/edit/<int:idDetalleCompras>', methods=['GET', 'POST'])
def edit(idDetalleCompras):
    detalle_compra = DetalleCompras.query.get_or_404(idDetalleCompras)

    if request.method == 'POST':
        detalle_compra.cantidadDetalle = request.form['cantidadDetalle']
        detalle_compra.subTotalDetalle = request.form['subTotalDetalle']
        detalle_compra.idProductos = request.form['idProductos']
        detalle_compra.idCompras = request.form['idCompras']

        db.session.commit()
        return redirect(url_for('DetalleCompras.index'))

    return render_template('DetalleCompras/edit.html', detalle_compra=detalle_compra)
    

@bp.route('/DetalleCompras/delete/<int:idDetalleCompras>')
def delete(idDetalleCompras):
    detalle_compra = DetalleCompras.query.get_or_404(idDetalleCompras)
    
    db.session.delete(detalle_compra)
    db.session.commit()

    return redirect(url_for('DetalleCompras.index'))
