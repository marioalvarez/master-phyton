#condicional IF

#color = input("adivina cual es mi color favorito?: ")
color = "rojo"
if color == "rojo":
    print("enhorabuena")
    print("el color es rojo")
else:
    print("el color no es rojo")

print("\n########## Ejemplo 2 ##############")

year = 2020
#year = int(input("en que año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("es un año anterior a 2021")

#if anidado
#ejemoplo 3
print("####### Ejemplo3 ##############")
#if anidado

nombre = "Mario Alvarez"
ciudad = "Chile"
continente = "america"
edad = 10
mayoria_edad = 19

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "america":
        print("el usuario No es americano")
    else:
        print(f" es Americano y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")


#elif

#dia = int(input("Introduce el numero del dia de la semana: "))
dia = 1
"""
if dia == 1 :
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("es jueves")
            else:
                if dia == 5:
                    print("es Viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("Es fin de semana")


#operadores logicos
#ejemoplo 5
print("####### Ejemplo5 ##############")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("tienes edad de trabajar? Introduce tu edad: "))

edad_oficial = 19

if edad_oficial >= 18 and edad_oficial <= 65:
    print("esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")




#ejemplo7
print("####### Ejemplo7 ##############")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana ")


#ejemplo6
print("####### Ejemplo6 ##############")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana "

#ejemplo 7
print("####### Ejemplo 7 ##############")

pais = "España"

if not (pais != "Mexico" or pais != "España" or pais != "Colombia"):
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana ")