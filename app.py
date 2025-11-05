from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    # Pantalla inicial con formulario
    return render_template('index.html')

@app.route('/offers', methods=['POST'])
def offers():
    # Captura los datos del formulario (no se guardan en DB)
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')
    email = request.form.get('email')
    banco = request.form.get('banco')
    
    # Redirige a la pantalla de resultados
    return render_template('results.html', nombre=nombre, apellido=apellido)

if __name__ == '__main__':
    # Flask corriendo en Termux
    app.run(host='0.0.0.0', port=5000)
