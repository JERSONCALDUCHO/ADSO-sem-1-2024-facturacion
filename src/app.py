from flask import Flask, render_template

app = Flask (__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/formulario_usuario')
def formulario_usuario():
    return render_template('formulario_usuario.html')

@app.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html')

@app.route('/formulario_factura')
def formulario_factura():
    return render_template('formulario_factura.html')

@app.route('/formulario_cliente')
def formulario_clientedex():
    return render_template('formulario_cliente.html')