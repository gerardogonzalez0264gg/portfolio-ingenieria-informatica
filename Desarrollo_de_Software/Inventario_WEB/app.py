from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos simulada en memoria (se borra si reinicias el servidor, pero ideal para aprender)
USUARIO_CORRECTO = "admin"
PASSWORD_CORRECTO = "1234"

inventario = [
    {"id": 1, "nombre": "Teclado Mecánico", "cantidad": 15, "precio": 45000},
    {"id": 2, "nombre": "Mouse Gamer", "cantidad": 30, "precio": 25000},
    {"id": 3, "nombre": "Monitor 24'' FHD", "cantidad": 8, "precio": 120000}
]

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        # Validamos las credenciales
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
            # Si es correcto, lo mandamos a la ruta del inventario
            return redirect(url_for("ver_inventario"))
        else:
            # Si es incorrecto, volvemos a cargar el login (podríamos pasar un mensaje de error)
            return render_template("login.html", error="Usuario o contraseña incorrectos")
        
    return render_template("login.html")

@app.route("/inventario", methods=["GET", "POST"])
def ver_inventario():
    if request.method == "POST":
        # Lógica para agregar un nuevo producto desde el formulario de inventario
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])
        
        nuevo_id = len(inventario) + 1
        nuevo_producto = {"id": nuevo_id, "nombre": nombre, "cantidad": cantidad, "precio": precio}
        inventario.append(nuevo_producto)
        
        return redirect(url_for("ver_inventario"))

    return render_template("inventario.html", productos=inventario)

if __name__ == "__main__":
    app.run(debug=True)