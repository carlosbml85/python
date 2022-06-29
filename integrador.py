
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





#funcion carlos        
def menu(lista):
    menuOpcion = 0
    while menuOpcion != 5:
        menuOpcion = (int(input("Ingrese el valor de que operación quiere realizar: \n 1-Sumar \n 2-Calcular Promedio \n 3-Calcular Máximo \n 4-Calcular Minimo \n 5-Salir  \n tipee uno de los valores:" + "\n")))
        if menuOpcion == 1:
            suma(lista)
        elif menuOpcion == 2:
            promedio(lista)
        elif menuOpcion == 3:
            maximo(lista)
        elif menuOpcion == 4:
            minimo(lista)
        else:
            menuOpcion == 5
            print("FIN")


lista = []
for i in range(5):
        valor = int(input("Ingrese números enteros: "))
        lista.append(valor)
        i += 1

menu(lista)
