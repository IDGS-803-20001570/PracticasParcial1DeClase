from flask import Flask,render_template,request
import forms
import math
app =Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def formulario():
    return render_template("formulario1.html")

@app.route("/distancia",methods=["GET","POST"])
def distancia():
    resultado = ""
    distancia_form=forms.distanciaPuntos(request.form)
    if request.method == 'POST':
        X1=distancia_form.X1.data
        X2=distancia_form.X2.data
        Y1=distancia_form.Y1.data
        Y2=distancia_form.Y2.data

        resultadoX= (int(X2)-int(X1))**2
        resultadoY= (int(Y2)-int(Y1))**2
        
        resultado = str(math.sqrt(resultadoX+resultadoY))

    return render_template("distancia.html",form=distancia_form,resultado=resultado)


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

@app.route("/Cine",methods=["GET","POST"])
def resultadoCine():
    if request.method == "POST":
        numeroBoletos= int(request.form.get("numBoletos"))
        tieneTarjetaCine= int(request.form.get("tarjetaCine"))
        precioBoleto = 12
        numCompradores = int(request.form.get("numCompradores"))
        boletosPermitidos = numCompradores*7

        #Valida descuento por cantidad de boletos
        if numeroBoletos <= boletosPermitidos:
            
            if numeroBoletos > 5:
                descuento = 0.15
            elif numeroBoletos in [3,4,5]:
                descuento = 0.10
            else:
                descuento = 0 

            subtotal = numeroBoletos*precioBoleto
            precioTotal = subtotal - (subtotal*descuento)
            
            descuentoTarjeta = 0.10 if (tieneTarjetaCine == 1) else 0
            

            if descuentoTarjeta == 0 :
                return render_template("cinepolis.html",res=precioTotal)
            else:
                #Calculamos Total 
                precioTotal = precioTotal - (precioTotal*descuentoTarjeta)
                return render_template("cinepolis.html", res=precioTotal)
        else:
            return render_template("cinepolis.html", res="La cantidad permitida de boletos por persona es de 7")
    #Petición GET devuelve la pagina.
    return render_template("cinepolis.html")


#Metodo que inicializa la aplicacion del proyecto

if __name__ == "__main__":
    app.run(debug=True)

