from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

usuario_correcto="admin"
contraseña_correcta="1234"

inventario=[]

@app.route("/", methods=["GET", "POST"])
def inicio():   

    if request.method=="POST":
    
        nombre = request.form['nombre']
        contraseña= request.form['contraseña']

        if nombre == usuario_correcto and contraseña == contraseña_correcta:
           return redirect(url_for("ver_inventario"))
        else:
            return render_template("login.html", error="Error usuario erraneo o no existente") 
    return render_template("login.html")

@app.route("/inventario", methods=["GET", "POST"])
def ver_inventario():
    if request.method=="POST":
        nombre=request.form["nombre"]
        cantidad=request.form["cantidad"]
        precio=request.form["precio"]

        nuevo_id=len(inventario)+1
        productos={
            "id":nuevo_id, 
            "nombre":nombre, 
            "cantidad":cantidad, 
            "precio":precio
        }
        inventario.append(productos)

    return render_template("inventario.html", producto=inventario)

if __name__ == "__main__":
   app.run(debug=True)