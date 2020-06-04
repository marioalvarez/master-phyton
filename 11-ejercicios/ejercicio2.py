"""
Ejericicio: Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
plus: usar while y for
"""
#while
coleccion = []
contador = 0
while contador < 120:
    coleccion.append(f"elemento-{contador}")
    print("mostrando el: " + coleccion[contador])
    contador += 1

print(coleccion[77])

#for
coleccion = []
for contador in range(0,120):
    coleccion.append(f"elemento-{contador}")
    print("mostrando el: " + coleccion[contador])

print(coleccion)
#mostrar el elemnto 115
print(coleccion[115])