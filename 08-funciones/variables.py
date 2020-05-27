"""
variables locales: Se definen dentro de la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro
A no ser que hagamos un return

variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas
"""

#Variable Global
frase = "ni los genios son tan genios"

print(frase)

def holaMundo():
    #frase = "Hola mundo!!"
    print("dentro de la funcion:")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "marioalvarez.cl"
    print("DENTRO: ", website)

    return "dato devuelto" + str(year)

holaMundo()
print(holaMundo())

print("FUERA: ", website)