
#funcion carlos
def cargarlista():
        for i in range(5):
                valor = int(input("Ingrese números enteros: "))
                lista.append(valor)
                i += 1

#funcion fara
def suma(lista):
        suma1 = 0
        for elem in lista:
                suma1 += elem
        print("La suma total de los valores es: " + str(suma1) + "\n") 
        
        
#funcion Christian
def maximo(lista):
    valorMax = max(lista)
    print("El valor máximo cargado en la lista es: " + str(valorMax) + "\n")

        

lista = []
cargarlista()
print(lista)
suma(lista)
maximo(lista)

