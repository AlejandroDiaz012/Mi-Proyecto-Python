from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Proveedores import Proveedores
from app import db

bp = Blueprint('Proveedores', __name__)

@bp.route('/Proveedores')
def index():
    data = Proveedores.query.all()
    # Proveedores_list = [Proveedores.to_dict() for book in data]
    # return jsonify(Proveedores_list)
    return render_template('Proveedores/index.html', data=data)

@bp.route('/Proveedores/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreProveedores = request.form['nombreProveedores']
        direccionProveedores = request.form['direccionProveedores']
        telefonoProveedores = request.form['telefonoProveedores']
        correoProveedores = request.form['correoProveedores']
        
        new_Proveedores = Proveedores(nombreProveedores=nombreProveedores, direccionProveedores=direccionProveedores, telefonoProveedores=telefonoProveedores, correoProveedores=correoProveedores)
        db.session.add(new_Proveedores)
        db.session.commit()
        
        return redirect(url_for('Proveedores.index'))

    return render_template('Proveedores/add.html')

@bp.route('/Proveedores/edit/<int:idProveedores>', methods=['GET', 'POST'])
def edit(idProveedores):
    proveedor = Proveedores.query.get_or_404(idProveedores)

    if request.method == 'POST':
        proveedor.nombreProveedores = request.form['nombreProveedores']
        proveedor.direccionProveedores = request.form['direccionProveedores']
        proveedor.telefonoProveedores = request.form['telefonoProveedores']
        proveedor.correoProveedores = request.form['correoProveedores']
       
        db.session.commit()
        return redirect(url_for('Proveedores.index'))

    return render_template('Proveedores/edit.html', proveedor=proveedor)
    

@bp.route('/Proveedores/delete/<int:idProveedores>')
def delete(idProveedores):
    proveedores = Proveedores.query.get_or_404(idProveedores)
    
    db.session.delete(proveedores)
    db.session.commit()

    return redirect(url_for('Proveedores.index'))
