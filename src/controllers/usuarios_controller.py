from flask import render_template, request
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from src.app import app

class ClientesController(FlaskController):
    @app.route('/formulario_usuario', methods=['GET', 'POST'])
    def formulario_usuario():
        if request.method == 'POST':
            nombres_usuario = request.form.get('nombres_usuario')
            apellidos_usuario = request.form.get('apellidos_usuario')
            numero_usuario = request.form.get('numero_usuario')
            email_usuario = request.form.get('email_usuario')
            tipo_documento_usuario = request.form.get('tipo_documento_usuario')
            num_documento_usuario = request.form.get('num_documento_usuario')
            nacimiento_usuario = request.form.get('nacimiento_usuario')
            contraseña_usuario = request.form.get('contraseña_usuario')
            confirmacion_contraseña = request.form.get('confirmacion_contraseña')
            usuario = Usuarios(nombres_usuario,apellidos_usuario,numero_usuario,email_usuario,tipo_documento_usuario,num_documento_usuario,nacimiento_usuario,contraseña_usuario,confirmacion_contraseña)
            Usuarios.crear_usuario(usuario)
        return render_template('formulario_usuario.html',titulo='Crear Usuario')

    @app.route('/inicio_sesion')
    def inicio_sesion():
        return render_template('inicio_sesion.html',titulo='Inicio sesion')