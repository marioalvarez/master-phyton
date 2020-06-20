from io import open
import pathlib
import shutil

#abrir archivo
#archivo = open("14-sistema-archivos/fichero_texto.txt","a+")

#abrir archivo en ruta absoluta
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo = open(ruta,"a+")
#print(ruta)

#escribir archivo
archivo.write("******soy un texto medito desde python*****\n")

#cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta,"r")
#print(ruta)

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
#archivo_lectura.close()

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)
    #print("- " +frase.upper())#pasar frase a mayus
    #pasar frase a lista

#copiar, renombrar y eliminar (Module shutil)
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto2.txt"

#ruta_alternativa = "../07-ejercicios/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Mover
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto2.txt"

shutil.move(ruta_original,ruta_nueva)

# Eliminar

import os

ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto2.txt"
os.remove(ruta_nueva)

#Comprobar si existe
import os.path

print(os.path.abspath("../"))

if os.path.isfile(os.path.abspath("./") + "Fichero_texto.txt"):
    print("El archivo existe")
else:
    print("el archivo no existe")