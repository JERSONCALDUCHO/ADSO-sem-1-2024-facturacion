from flask import render_template, request
from flask_controller import FlaskController
from src.models.clientes import Clientes
from src.app import app


class ClientesController(FlaskController):
    @app.route('/formulario_cliente', methods=['GET','POST'])
    def formulario_cliente():
        if request.method == 'POST':
            nombres_cliente = request.form.get('nombres_cliente')
            apellidos_cliente = request.form.get('apellidos_cliente')
            numero_cliente = request.form.get('numero_cliente')
            email_cliente = request.form.get('email_cliente')
            tipo_documento_cliente = request.form.get('tipo_documento_cliente')
            num_documento_cliente = request.form.get('num_documento_cliente')
            nacimiento_cliente = request.form.get('nacimiento_cliente')
            cliente = Clientes(nombres_cliente,apellidos_cliente,numero_cliente,email_cliente,tipo_documento_cliente,num_documento_cliente,nacimiento_cliente)
            Clientes.crear_cliente(cliente)
        return render_template('formulario_cliente.html',titulo='Crear Cliente')
    
    @app.route('/lista_clientes')
    def lista_clientes():
        try:
            clientes = Clientes.traer_clientes()
            return render_template('lista_clientes.html',titulo='Ver clientes', clientes = clientes)
        except:
            return render_template('lista_clientes.html',titulo='Error de conexión a la base de datos')  
    
