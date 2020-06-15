from io import open
import pathlib

#abrir archivo
#archivo = open("14-sistema-archivos/fichero_texto.txt","a+")

#abrir archivo en ruta absoluta
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")
print(ruta)

#escribir archivo
archivo.write("******soy un texto medito desde python*****\n")