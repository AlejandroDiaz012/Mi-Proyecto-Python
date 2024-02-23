from app import db


class DetalleVentas(db.Model):
    __tablename__ = 'detalle_venta'
    idDetalleVentas = db.Column(db.Integer, primary_key=True)
    cantidadDetalle = db.Column(db.Integer, nullable=False)
    subTotalDetalle = db.Column(db.Integer, nullable=False)
    idVentas = db.Column(db.Integer, db.ForeignKey('venta.idVentas'))
    idProductos = db.Column(db.Integer, db.ForeignKey('producto.idProductos'))
    producto = db.relationship('Productos')
    