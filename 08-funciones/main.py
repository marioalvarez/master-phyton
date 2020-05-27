"""
una funcion es un conjunto de instrucciones bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tntas veces como sea necesario.
"""

#ejemplo 1

print("#### ejemplo 1 ####")

def muestraNombre():
    print("Super")
    print("Mario")
    print("Lucy")
    print("Tina")
    print("\n")

#invocar funciones
muestraNombre()
muestraNombre()
muestraNombre()

"""
#ejemplo 2
print("#### ejemplo 2 ####")


def mostrarTuNombre(nombre, edad):
    print(f"tu nombre es:{nombre}")

    if edad >= 18:
        print("y es mayor de edad")
nombre = input("introduce tu nombre: ")
edad = int(input("introduce tu edad: "))

mostrarTuNombre(nombre, edad)
"""
#ejemplo 3
print("#### ejemplo 3 ####")

def tabla(numero):
    print(f"tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")
"""
numero_usuario = int(input("ingresa el numero para ver la tabla: "))
tabla(numero_usuario)
"""

#ejemplo 3.1
print("#### ejemplo 3.1 ####")

for numero_tabla in range(1,11):
    tabla(numero_tabla)


#ejemplo 4
print("#### ejemplo 4 ####")

#parametros opcionales

def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Mario Alvarez","1-9")

#ejemplo 5
print("#### ejemplo 5 ####")
#Ejemplo 5: parametros opcionales y return o devolver datos

def saludame(nombre):
    saludo = f"Hola saludos {nombre}"

    return saludo

print(saludame("Mario alvarez"))

#ejemplo 6
print("#### ejemplo 6 ####")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:        
        cadena += "Multiplicacion " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(5,5, False))


#ejemplo 7
print("\n#### ejemplo 7 ####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("mario","Alvarez Zapata"))

#ejemplo 8: Funciones Lambda
print("\n#### ejemplo 8 ####")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))
