from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        tarros = int(request.form.get("cantidad"))
        precio_tarro = 9000
        total_sin_descuento = precio_tarro * tarros

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_descuento = total_sin_descuento * (1 - descuento)

        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            total_descuento=total_descuento,
            calculado=True
        )
    return render_template("ejercicio1.html", calculado=False)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template("ejercicio2.html", mensaje=mensaje)

    return render_template("ejercicio2.html", mensaje=None)

if __name__ == "__main__":
    app.run(debug=True)


