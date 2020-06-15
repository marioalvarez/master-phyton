"""
Modulos: son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html
"""
#importar mi modulo propio
#Llamar al modulo completo
#import miModulo

#Llamar a una funcion de un modulo
from miModulo import holaMundo

#Llamar las funciones sin modulo adelante
from miModulo import*

#imprimir llamando a todo el modulo
#print(miModulo.holaMundo("mario alvarez"))
#print(miModulo.calculadora(3,5,True))

#imprimir llamando a la funcion especifica
#print(holaMundo("Mario Alvarez"))

#imprimir llamando a todas las funciones del modulo con *
#print(holaMundo("mario alvarez"))
#print(calculadora(3,5,True))

#Modulo de Fechas
import datetime

#hoy
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
"""
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, ")
print(f"Mi fecha personalizada: {fecha_personalizada}")

print(datetime.datetime.now().timestamp())
"""
#modulo Matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", math.pi)
#redondear al alza
print("Redondeo del numero  : ", math.ceil(6.65789))
#redondear a la baja
print("Redondeo a la baja del numero  : ", math.floor(6.66881))

#modulo random
import random 
print("numero aleatorio entre 15 y 67: ", random.randint(15,67))