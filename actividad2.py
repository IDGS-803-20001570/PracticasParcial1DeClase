class OperaNumeros:
    #Declaración de propiedades de clase 
    lstNumeros=[]
    lstNumPares=[]
    diccionarioRepeticiones={}
    numerosLeidos=set()
    num1=0
    #Declaración de contructor
    def __init__(self,a):
        self.num1=a
    #Declaración de métodos de clase
    def llenarLista(self):        
        for i in range(self.num1):
            num = int(input("Ingresa un número: "))
            self.lstNumeros.append(num)
        print("La lista es:\n",self.lstNumeros)
    def ordenarLista(self):
        self.lstNumeros.sort()
        print("La lista ordenada es:\n",self.lstNumeros)
    def repeticiones(self):
        for i in self.lstNumeros:
            if self.lstNumeros.count(i) != 1 and i not in self.numerosLeidos:
                self.diccionarioRepeticiones[i]=self.lstNumeros.count(i)
                self.numerosLeidos.add(i)
                print("El número {} se repite {} veces.".format(i,self.lstNumeros.count(i)))
    def numPares(self):
        for i in self.lstNumeros:
            if i % 2 == 0:
                self.lstNumPares.append(i)
        print("Se encontraron {} números pares.".format(len(self.lstNumPares)))
        print("Los números pares son: \n",self.lstNumPares)

def main():
    obj=OperaNumeros(5)
    obj.llenarLista()
    obj.ordenarLista()
    obj.repeticiones()
    obj.numPares()

if __name__=="__main__":
    main()

    #PracticasParcial1DeClase
    ##Ejercicio 1 ingresar número imrimir astericos * 1 en 1 hasta el número
    #Programa que lea la 10 números [lista] primero ordenarlos, cuales son pares, cuantos números se repiten y el número de veces que se repiten 