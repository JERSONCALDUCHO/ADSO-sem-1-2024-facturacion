from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

app = Flask (__name__)

if __name__ == '__main__':
    app.run(debug=True)

engine = create_engine("mysql+pymysql://root@localhost/factura_001?charset=utf8mb4")

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadate.bind = engine


@app.route('/')
def index():
    return render_template('index.html',titulo='Bienvenido a la aplicación de facturación')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html',titulo='Listado de Productos')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html',titulo='Inicio sesion')

@app.route('/formulario_usuario')
def formulario_usuario():
    return render_template('formulario_usuario.html',titulo='Crear Usuario')

@app.route('/formulario_producto')
def formulario_producto():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        print ("Entro por POST")
        print(codigo)
    return render_template('formulario_producto.html',titulo='Crear Producto')

@app.route('/formulario_factura')
def formulario_factura():
    return render_template('formulario_factura.html',titulo='Generar factura')

@app.route('/formulario_cliente')
def formulario_cliente():
    return render_template('formulario_cliente.html',titulo='Crear Cliente')

@app.route('/lista_clientes')
def lista_clientes():
    return render_template('lista_clientes.html',titulo='Ver clientes')

class Productos(Base):
    __tablename__: "productos"
    id = Column (Integer, primary_key=True)
    codigo = Column (String(9), unique=True, nullable=False)
    descripcion = Column (String(300), unique=True)
    valor_unitario = Column (Float(10,8))
    unidad_medida = Column (String(3), unique=True, nullable=False)
    cantidad_stock = Column (Float(10,8))
    categoria = Column (Integer, nullable=False)

class Categoria(Base):
    __tablename__: "categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)
    
Base.metadate.create_all(engine)