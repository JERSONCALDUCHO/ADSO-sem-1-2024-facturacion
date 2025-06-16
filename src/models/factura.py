from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from src.models import session, Base
from src.models.clientes import Clientes
from src.models.productos import Productos

class Facturas(Base):
    __tablename__ = "factura"
    id = Column (Integer, primary_key=True)
    fecha_hora = Column (DateTime, nullable=False)
    id_cliente = Column (Integer, ForeignKey('clientes.id'), nullable=False)
    id_producto = Column (Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column (Float(10,8), nullable=False)

    def __init__(self,fecha_hora,id_cliente,id_producto,cantidad):
        self.fecha_hora = fecha_hora
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.cantidad = cantidad

    def crear_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura