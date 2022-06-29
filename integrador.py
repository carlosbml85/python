
#funcion carlos
lista = []
def cargarlista():
        
        for i in range(5):
                valor = int(input("Ingrese números enteros: "))
                lista.append(valor)
                i += 1

def suma(lista):
        suma1 = 0
        for elem in lista:
                suma1 += elem
        print("La suma total de los valores es: " + str(suma1) + "\n") 



cargarlista()
print(lista)
suma(lista)
    