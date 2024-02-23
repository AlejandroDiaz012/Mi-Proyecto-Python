from app import db
from flask_login import UserMixin

class Empleados(db.Model,UserMixin): 
    __tablename__ = 'empleado'
    idEmpleados = db.Column(db.Integer, primary_key=True)
    nombreEmpleados = db.Column(db.String(255), nullable=False)
    direccionEmpleados = db.Column(db.String(255), nullable=False)
    telefonoEmpleados = db.Column(db.String(255), nullable=False)
    contrasenaEmpleados = db.Column(db.String(255), nullable=False)
    ventas = db.relationship("Ventas", back_populates="empleados")
        
    def get_id(self):
        return str(self.idEmpleados)