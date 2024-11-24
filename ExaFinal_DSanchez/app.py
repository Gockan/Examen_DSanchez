from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_ejercicio1', methods=['GET', 'POST'])
def procesar_ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        # Determinar el descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        # Enviar los resultados a la plantilla
        return render_template(
            '/ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            monto_descuento=int(monto_descuento),
            total_con_descuento=int(total_con_descuento),
        )
    return render_template('/ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    usuario = request.form['usuario']
    password = request.form['password']
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if usuario in usuarios and usuarios[usuario] == password:
        if usuario == "juan":
            mensaje = f"Bienvenido administrador {usuario}"
        else:
            mensaje = f"Bienvenido usuario {usuario}"
    else:
        mensaje = "Credenciales incorrectas"

    # Devolver el mensaje a la plantilla junto con el formulario
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
