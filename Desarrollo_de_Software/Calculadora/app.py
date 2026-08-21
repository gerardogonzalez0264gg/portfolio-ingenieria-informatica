from flask import Flask, render_template,request

app=Flask(__name__)

def suma(a, b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def porcentaje(a,b):
    return (a*100)/b

@app.route("/", methods=["POST", "GET"])
def index():
    res=None
    if request.method=="POST":
        a=int(request.form["a"])
        b=int(request.form["b"])

        operacion=request.form["operacion"]

        if operacion == "suma":
            res=suma(a,b)
        elif operacion == "resta":
            res=resta(a,b)
        elif operacion == "multiplicacion":
            res=multiplicacion(a,b) 
        elif operacion == "division":
            res=division(a,b)
        elif operacion == "porcentaje":
            res=porcentaje(a,b)
    return render_template("index.html", res=res)

if __name__=="__main__":
    app.run(debug=True)


