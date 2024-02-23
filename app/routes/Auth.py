from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Clientes import Clientes
from app.models.Empleados import Empleados

bp = Blueprint('Auth', __name__)
@bp.route('/', methods=['GET', 'POST'])
def login():
    global tipodeusuario
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        
        empleados = Empleados.query.filter_by(nombreEmpleados=nombre, contrasenaEmpleados=contrasena).first()
    
        if empleados:
            login_user(empleados)
            flash("Login successful!", "success")
            tipodeusuario = 1
            print("Entra a empleado ", current_user.idEmpleados)
            return redirect(url_for('Empleados.index'))
        clientes = Clientes.query.filter_by(nombreClientes=nombre, contrasenaClientes=contrasena).first()

        if clientes:
            login_user(clientes)
            print(current_user.nombreClientes)            
            tipodeusuario = 0
            print("Entra a Cliente", current_user.idClientes)
            return redirect(url_for('Productos1.index'))
        flash('Invalid credentials. Please try again.','danger')
    return render_template("Auth/login.html")

@bp.route('/Iniciar')
@login_required
def Iniciar():
     return redirect(url_for('Productos1.index'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return render_template("Auth/login.html")
