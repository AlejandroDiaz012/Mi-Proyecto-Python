from app import db

class Proveedores(db.Model):
    __tablename__ = 'proveedor'
    idProveedores = db.Column(db.Integer, primary_key=True)
    nombreProveedores = db.Column(db.String(255), nullable=False)
    direccionProveedores = db.Column(db.String(255), nullable=False)
    telefonoProveedores = db.Column(db.String(255), nullable=False)
    correoProveedores = db.Column(db.String(255), nullable=False)
    