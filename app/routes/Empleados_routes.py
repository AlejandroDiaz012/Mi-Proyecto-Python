from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user
from app.models.Empleados import Empleados
from app import db

bp = Blueprint('Empleados', __name__)

@bp.route('/Empleados')
def index():    
    try: 
        current_user.idEmpleados
        data = Empleados.query.all()
        return render_template('Empleados/index.html', data=data)
    except:
        return redirect(url_for('Productos1.index'))

@bp.route('/Empleados/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreEmpleados = request.form['nombreEmpleados']
        direccionEmpleados = request.form['direccionEmpleados']
        telefonoEmpleados = request.form['telefonoEmpleados']
        contrasenaEmpleados = request.form['contrasenaEmpleados']

        new_Empleados = Empleados(nombreEmpleados=nombreEmpleados, direccionEmpleados=direccionEmpleados, telefonoEmpleados=telefonoEmpleados, contrasenaEmpleados=contrasenaEmpleados)
        db.session.add(new_Empleados)
        db.session.commit()
        
        return redirect(url_for('Empleados.index'))

    return render_template('Empleados/add.html')

@bp.route('/Empleados/edit/<int:idEmpleados>', methods=['GET', 'POST'])
def edit(idEmpleados):
    empleado = Empleados.query.get_or_404(idEmpleados)

    if request.method == 'POST':
        empleado.nombreEmpleados = request.form['nombreEmpleados']
        empleado.direccionEmpleados = request.form['direccionEmpleados']
        empleado.telefonoEmpleados = request.form['telefonoEmpleados']
        empleado.contrasenaEmpleados = request.form['contrasenaEmpleados']

        db.session.commit()
        return redirect(url_for('Empleados.index'))

    return render_template('Empleados/edit.html', empleado=empleado)
    

@bp.route('/Empleados/delete/<int:idEmpleados>')
def delete(idEmpleados):
    empleados = Empleados.query.get_or_404(idEmpleados)
    
    db.session.delete(empleados)
    db.session.commit()

    return redirect(url_for('Empleados.index'))
