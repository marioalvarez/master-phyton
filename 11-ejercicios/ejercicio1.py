"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
hecho-Recorrer la lista y mostrarla
hecho-hacer una funcion que recorra listas de numeros y devuelva un string
hecho-ordenarla y mostrarla
hecho-mostrar su longitud
hecho-buscar algun elemento ( que el usuario pida por teclado)
"""
#Crear la lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

#crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado= ""

    #for numero in numeros: cambiamos a datos genericos para abstraer la funcion
    for elemento in lista:   
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado

#recorrer y mostrar
print("### recorrer y mostrar ###")

"""
for numero in numeros:
    print(numero)
"""
print(mostrarLista(numeros))
print(mostrarLista(['victor','juan','pepe']))

#Parte2
#Ordenar y mostrar
print("### Ordenar y mostrar ###")
numeros.sort()
print(mostrarLista(numeros))

#Mostrar su longitud
print("### Mostrar su longitud ###")
print(len(numeros))

#Busqueda en la lista
print("### Busqueda en la lista ###")
busqueda = int(input("introduce un numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("introduce un numero: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"### Buscar en la lista el numero {busqueda} ###")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indice: {search}")




