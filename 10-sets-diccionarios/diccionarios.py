"""
Array asociativo o objeto de json
clave +valor 

Es un tipo de datos que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json
"""
persona = {
    "nombre":"Mario",
    "apellidos":"Alvarez",
    "web":"marioalvarez.cl"
}

print(persona)
print(type(persona))

#acceder al indice apellidos
print(persona["apellidos"])
print(persona["web"])


#lista con diccionarios

contactos = [
    {
        'nombre':'antonio',
        'email':'mario@mario.com'
    },
    {
        'nombre':'Luis',
        'email':'luis@luis.com'
    },
    {
        'nombre':'salvador',
        'email':'salva@salvador.com'
    }
]

#imprimir el array asociativo
print(contactos)

#acceder al usuario del contacto antonio y sacar su nombre
print(contactos[0]['nombre'])

#modificar el valor la propiedad
contactos[0]['nombre']= "Toño"
print(contactos[0]['nombre'])

#imprimir el listado de contactos
print("\nListado de Contactos: ")
print("________________________")

for contacto in contactos:
    print(f"Nombre del contaco:{contacto['nombre']} ")
    print(f"Email de contacto: {contacto['email']}")
    print("______________________________________")