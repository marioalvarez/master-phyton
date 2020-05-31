"""
Listas(arrays)
Colecciones o conjuntos de datos/valores bajo un unico nombre
para acceder a esos datos podemos usar indice numerico
"""
pelicula = "batman"

#definir una lista
peliculas = ["batman","spiderman","el señor de los anillos"]

#Funcion list
cantantes = list(('2pac','drake','jennifer lopez'))
years = list(range(2000,2020))

#variada
variada = ["nombres", 12, 15.5, "pepe",True]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
#indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(cantantes[1:])

#modificar variables
peliculas[1] = "Gran Torino"
print(peliculas)

#añadir elementos a una lista
cantantes.append("kase O")
cantantes.append("Natos y Waor")
print(cantantes)

"""
#recorrer listas
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


print("\n*********Listado de peliculas*********")
for pelicula in peliculas:
    print(f" {peliculas.index(pelicula)+1}. {pelicula}")

"""

#listas multidimensionales
print("\n########Listas de contactos##########")
contactos = [
    [
        'antonio',
        'antonio@anto.com'
    ],
    [
        'luis',
        'luis@luis.com'
    ],
    [
        'salvador',
        'salvador@salvador.com'
    ]
]
#print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Correo: " + elemento)
    print("\n")