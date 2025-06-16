from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.models import session, Base

class Clientes(Base):
    __tablename__ = "clientes"
    id = Column (Integer, primary_key=True)
    nombres_cliente = Column (String(300), nullable=False)
    apellidos_cliente = Column (String(300), nullable=False)
    numero_cliente = Column (String(15), nullable=False)
    email_cliente = Column (String(100), nullable=False)
    tipo_documento_cliente = Column (String(30), nullable=False)
    num_documento_cliente = Column (String(15), nullable=False)
    nacimiento_cliente = Column (Date, nullable=False)

    def __init__(self,nombres_cliente,apellidos_cliente,numero_cliente,email_cliente,tipo_documento_cliente,num_documento_cliente,nacimiento_cliente):
        self.nombres_cliente = nombres_cliente
        self.apellidos_cliente = apellidos_cliente
        self.numero_cliente = numero_cliente
        self.email_cliente = email_cliente
        self.tipo_documento_cliente = tipo_documento_cliente
        self.num_documento_cliente = num_documento_cliente
        self.nacimiento_cliente = nacimiento_cliente

    def crear_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente

    def traer_clientes():
        clientes = session.query(Clientes).all()
        return clientes
