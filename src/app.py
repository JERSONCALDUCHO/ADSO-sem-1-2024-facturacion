from flask import Flask, render_template

app = Flask (__name__)

if __name__ == '__main__':
    app.run(debug=True)

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
    return render_template('formulario_producto.html',titulo='Crear Producto')

@app.route('/formulario_factura')
def formulario_factura():
    return render_template('formulario_factura.html',titulo='Generar factura')

@app.route('/formulario_cliente')
def formulario_clientedex():
    return render_template('formulario_cliente.html',titulo='Crear Cliente')