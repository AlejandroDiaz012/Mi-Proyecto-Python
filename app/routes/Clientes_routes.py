from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from app.models.Clientes import Clientes
from flask_login import login_required
from app import db
app = Flask(__name__)

bp = Blueprint('Clientes', __name__)

@bp.route('/Clientes')
@login_required
def index():
    print("Entra a clientes")
    data = Clientes.query.all()
    print("Entra a clientes")

    # Clientes_list = [Clientes.to_dict() for book in data]
    # return jsonify(Clientes_list)
    return render_template('Clientes/index.html', data=data)

@bp.route('/Clientes/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreClientes = request.form['nombreClientes']
        direccionClientes = request.form['direccionClientes']
        telefonoClientes = request.form['telefonoClientes']
        correoClientes = request.form['correoClientes']
        contrasenaClientes = request.form['contrasenaClientes']

        new_Clientes = Clientes(nombreClientes=nombreClientes, direccionClientes=direccionClientes, telefonoClientes=telefonoClientes, correoClientes=correoClientes, contrasenaClientes=contrasenaClientes)
        db.session.add(new_Clientes)
        db.session.commit()
        
        return redirect(url_for('Clientes.index'))

    return render_template('Clientes/add.html')

@bp.route('/Clientes/edit/<int:idClientes>', methods=['GET', 'POST'])
def edit(idClientes):
    cliente = Clientes.query.get_or_404(idClientes)

    if request.method == 'POST':
        cliente.nombreClientes = request.form['nombreClientes']
        cliente.direccionClientes = request.form['direccionClientes']
        cliente.telefonoClientes = request.form['telefonoClientes']
        cliente.correoClientes = request.form['correoClientes']
        cliente.contrasenaClientes = request.form['contrasenaClientes']

        db.session.commit()
        return redirect(url_for('Clientes.index'))

    return render_template('Clientes/edit.html', cliente=cliente)
    

@bp.route('/Clientes/delete/<int:idClientes>')
def delete(idClientes):
    clientes = Clientes.query.get_or_404(idClientes)
    
    db.session.delete(clientes)
    db.session.commit()

    return redirect(url_for('Clientes.index'))


