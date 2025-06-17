from flask import render_template, request
from flask_controller import FlaskController
from src.models.factura import Facturas
from src.models.productos import Productos
from src.models.clientes import Clientes
from src.app import app

class FacturasController(FlaskController):
    @app.route('/formulario_factura', methods=['GET','POST'])
    def formulario_factura():
        clientes = Clientes.traer_clientes()
        productos = Productos.traer_productos()
        if request.method == 'POST':
            fecha_hora = request.form.get('fecha_hora')
            cliente = request.form.get('cliente')
            producto = request.form.get('producto')
            cantidad = request.form.get('cantidad')
            factura = Facturas(fecha_hora,cliente,producto,cantidad)
            Facturas.crear_factura(factura)
        return render_template('formulario_factura.html',titulo='Generar factura',productos = productos,clientes = clientes)
    
    @app.route('/lista_facturas')
    def lista_facturas():
        try:
            facturas = Facturas.traer_facturas()
            return render_template('lista_facturas.html',titulo = 'Ver facturas', facturas = facturas)
        except:
            return render_template('lista_facturas.html',titulo = 'Error de conexión a la base de datos')