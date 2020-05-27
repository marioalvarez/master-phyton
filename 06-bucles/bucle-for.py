"""

#FOR

for variable in elemento_iterable (lista, rango, etc)
    Bloque de instrucciones

"""
contador = 0
resultado = 0
for contador in range(0,5):
    print("voy por el "+str(contador))

    resultado = resultado + contador
print(f"El resultado es: {resultado}")


# Ejemplo tablas de multiplicar
print("\n###### EJMPLO #######")

numero_usuario = int(input("De qe numero quiers la tabla?: "))

if numero_usuario < 1:
    numero_usuario  = 1

print(f" \n### tabla de multiplicar del numero {numero_usuario} ###")

for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("no se pueden mostrar numeros prohibidos")
        break
    
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("tabla finalizada.")