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

print(fecha_completa)
print(fecha_completa.year)