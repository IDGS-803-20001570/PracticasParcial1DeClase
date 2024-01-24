from flask import Flask,render_template,request

app =Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2= request.form.get("n2")
        operacion= request.form.get("operaciones")
        if str(operacion) == "+":
            msj = "suma"
            resultado = int(num1)+int(num2)
        elif str(operacion) == "-":
            msj = "resta"
            resultado = int(num1)-int(num2)
        elif str(operacion) == "*":
            msj = "multiplicacion"
            resultado = int(num1)*int(num2)
        elif str(operacion) == "/":
            msj = "división"
            resultado = int(num1)/int(num2)

        
        return "<h1>La {} es: {} </h1>".format(msj,str(resultado))

#Metodo que inicializa la aplicacion del proyecto

if __name__ == "__main__":
    app.run(debug=True)

