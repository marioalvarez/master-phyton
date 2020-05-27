"""
Una variables es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""
texto = "Master en Python"
texto = 1

texto2 = "las variables no pueden comenzar en numeros"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)


# Concatenacion

nombre = "mario"
apellidos = "alvarez"
web = "marioalvarez.cl"

#concatenacion
print(nombre + " " + apellidos + " - " + web)

#funcion F
print(f"{nombre} {apellidos} - {web}")

#metodo format
print("Hola me llamo {}{} y mi web es {}".format(nombre, apellidos, web))


