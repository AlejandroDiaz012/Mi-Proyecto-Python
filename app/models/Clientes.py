from app import db
from flask_login import UserMixin

class Clientes(db.Model, UserMixin):
    __tablename__ = 'cliente'
    idClientes = db.Column(db.Integer, primary_key=True)
    nombreClientes = db.Column(db.String(255), nullable=False)
    direccionClientes = db.Column(db.String(255), nullable=False)
    telefonoClientes = db.Column(db.String(255), nullable=False)
    correoClientes = db.Column(db.String(255), nullable=False)
    contrasenaClientes = db.Column(db.String(255), nullable=False)
    ventas = db.relationship("Ventas", back_populates="clientes")
   
    def get_id(self):
        return str(self.idClientes)