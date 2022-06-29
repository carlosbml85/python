lista = []
for i in range(5):
        valor = int(input("Ingrese nùmero enteros: "))
        lista.append(valor)
        i += 1
print(lista)        
    

def suma(lista):
        suma1 = 0
        for elem in lista:
                suma1 += elem
        print("La suma total de los valores es: " + str(suma1) + "\n") 


suma()
    