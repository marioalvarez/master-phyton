"""
ejercicio 7
mostrar todos los numeros impares entre 2 numeros que el usuario ingrese
"""

numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))

if numero1 < numero2:
    for x in range(numero1,(numero2+1)):
        if x % 2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")           

else:
    print("el numero 1 debe ser mayor que el numero 2")