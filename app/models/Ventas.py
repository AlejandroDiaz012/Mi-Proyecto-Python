from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Ventas(db.Model):
    __tablename__ ='venta'
    idVentas = db.Column(db.Integer, primary_key=True)
    fechaVentas = db.Column(db.Date, nullable=False, default=func.now())
    cantidadVentas = db.Column(db.Integer, nullable=False)
    idClientes = db.Column(db.Integer, db.ForeignKey('cliente.idClientes'))
    idEmpleados = db.Column(db.Integer, db.ForeignKey('empleado.idEmpleados'))
    total = db.Column(db.Integer, nullable=False)   
    clientes = db.relationship("Clientes", back_populates="ventas")
    empleados = db.relationship("Empleados", back_populates="ventas")
    productos = db.relationship("Productos", secondary="detalle_venta", back_populates="ventas")
