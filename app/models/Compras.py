from app import db


class Compras(db.Model):
    __tablename__ ='compra'
    idCompras = db.Column(db.Integer, primary_key=True)
    fechaCompras = db.Column(db.Date, nullable=False)
    cantidadCompras = db.Column(db.Integer, nullable=False)
    idProveedores = db.Column(db.Integer, db.ForeignKey('proveedor.idProveedores'))
    idEmpleados = db.Column(db.Integer, db.ForeignKey('empleado.idEmpleados'))
    