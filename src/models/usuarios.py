from sqlalchemy import Column, Integer, String, Date
from src.models import session, Base

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column (Integer, primary_key=True)
    nombres_usuario = Column (String(300), nullable=False)
    apellidos_usuario = Column (String(300), nullable=False)
    numero_usuario = Column (Integer, nullable=False)
    email_usuario = Column (String(100), nullable=False)
    tipo_documento_usuario = Column (String(30), nullable=False)
    num_documento_usuario = Column (Integer, nullable=False)
    nacimiento_usuario = Column (Date, nullable=False)
    contraseña_usuario = Column (String(30), nullable=False)
    confirmacion_contraseña = Column (String(30), nullable=False)

    def __init__(self,nombres_usuario,apellidos_usuario,numero_usuario,email_usuario,tipo_documento_usuario,num_documento_usuario,nacimiento_usuario,contraseña_usuario,confirmacion_contraseña):
        self.nombres_usuario = nombres_usuario
        self.apellidos_usuario = apellidos_usuario
        self.numero_usuario = numero_usuario
        self.email_usuario = email_usuario
        self.tipo_documento_usuario = tipo_documento_usuario
        self.num_documento_usuario = num_documento_usuario
        self.nacimiento_usuario = nacimiento_usuario
        self.contraseña_usuario = contraseña_usuario
        self.confirmacion_contraseña = confirmacion_contraseña

    def crear_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario
