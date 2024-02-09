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

@app.route("/resistencias",methods=["GET","POST"])
def resistencias():
    resultado = ""
    valorMinimo=""
    valorMaximo=""

    # Diccionario para mapear los colores a códigos hexadecimales
    colores_hex = {
        '0': {'nombre': 'Negro', 'hex': '#000000'},
        '1': {'nombre': 'Cafe', 'hex': '#804000'},
        '2': {'nombre': 'Rojo', 'hex': '#FF0000'},
        '3': {'nombre': 'Naranja', 'hex': '#FFA500'},
        '4': {'nombre': 'Amarillo', 'hex': '#FFFF00'},
        '5': {'nombre': 'Verde', 'hex': '#008000'},
        '6': {'nombre': 'Azul', 'hex': '#0000FF'},
        '7': {'nombre': 'Violeta', 'hex': '#EE82EE'},
        '8': {'nombre': 'Gris', 'hex': '#808080'},
        '9': {'nombre': 'Blanco', 'hex': '#FFFFFF'},
        'oro': {'nombre': 'Oro', 'hex': '#FFD700'},
        'plata': {'nombre': 'Plata', 'hex': '#C0C0C0'}
    }

    colores_hexa = {
        '1': {'nombre': 'Negro', 'hex': '#000000'},
        '10': {'nombre': 'Cafe', 'hex': '#804000'},
        '100': {'nombre': 'Rojo', 'hex': '#FF0000'},
        '1000': {'nombre': 'Naranja', 'hex': '#FFA500'},
        '10000': {'nombre': 'Amarillo', 'hex': '#FFFF00'},
        '100000': {'nombre': 'Verde', 'hex': '#008000'},
        '1000000': {'nombre': 'Azul', 'hex': '#0000FF'},
        '10000000': {'nombre': 'Violeta', 'hex': '#EE82EE'},
        '100000000': {'nombre': 'Gris', 'hex': '#808080'},
        '1000000000': {'nombre': 'Blanco', 'hex': '#FFFFFF'}
    }

    registros=[]

    resistencias_form=forms.calculaResistencias(request.form)
    if request.method == 'POST':
        color1=resistencias_form.color1.data
        color2=resistencias_form.color2.data
        color3=resistencias_form.color3.data
        
        valorColores = int(str(color1+color2))*int(color3)
        tolerancia= request.form.get("tolerancia")
        
        if str(tolerancia) == "oro":
            valorMinimo = valorColores - (valorColores*0.05)
            valorMaximo = valorColores + (valorColores*0.05)
        elif str(tolerancia) == "plata":
            valorMinimo = valorColores - (valorColores*0.10)
            valorMaximo = valorColores + (valorColores*0.10)

        registros.append({
            "color1": colores_hex[color1]['nombre'],
            "color2": colores_hex[color2]['nombre'],
            "color3": colores_hexa[color3]['nombre'],
            "tolerancia":tolerancia,
            "valor":valorColores,
            "valorMinimo":valorMinimo,
            "valorMaximo":valorMaximo,
            "colorCelda1": colores_hex[color1]['hex'],
            "colorCelda2": colores_hex[color2]['hex'],
            "colorCelda3": colores_hexa[color3]['hex'],
            "colorCelda4": colores_hex[tolerancia]['hex']
        })
        

    return render_template("resistencias.html",form=resistencias_form,registros=registros)

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

