class OperaAstericos:
    #Declaración de propiedades de clase 
    num1=0
    #Declaración de contructor
    def __init__(self,a):
        self.num1=a
    #Declaración de métodos de clase
    def astericos(self):
        valor = "*"
        for i in range(self.num1+1):
            print(valor*i)
def main():
    obj=OperaAstericos(3)
    obj.astericos()

if __name__=="__main__":
    main()

    #PracticasParcial1DeClase
    ##Ejercicio 1 ingresar número imrimir astericos * 1 en 1 hasta el número
    #Programa que lea la 10 números [lista] primero ordenarlos, cuales son pares, cuantos números se repiten y el número de veces que se repiten 