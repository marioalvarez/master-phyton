
"""
escribir un programa que muestre los cuadrados
de los 60 primeros numeros naturales 
* resolverlo con for y while
"""
#while
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f" el cuadrado de {contador} es {cuadrado}")

    contador += 1

#for
for contador in range(0,60):
    cuadrado = contador * contador
    print(f"el numero cuadrado de {contador} es {cuadrado}")
else:
    print("fin del contadorcon for")