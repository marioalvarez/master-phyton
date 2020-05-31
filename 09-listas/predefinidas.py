cantantes = ['2pac','drake','bad bunny','julio iglesias']
numeros = [1,2,5.5,6,3,4]

#ordenar
print(numeros)
numeros.sort()
print(numeros)

#añadir elementos
cantantes.append("mario alvarez")
cantantes.insert(1, "super mario")
print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove('bad bunny')
print(cantantes)

#Darle la vuelta al arreglo
print(numeros)
numeros.reverse()
print(numeros)

#buscar dentro de una lista
print('drake' in cantantes)

#contar elementos
print(cantantes)
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#conseguir indice
print(cantantes.index("drake"))

#unir listas
cantantes.extend(numeros)
print(cantantes)