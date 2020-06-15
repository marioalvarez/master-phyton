from io import open
import pathlib

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