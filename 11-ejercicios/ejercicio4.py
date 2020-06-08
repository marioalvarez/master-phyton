"""
Ejericio 4
Crear un script que tenga 4 variables una lista un string
un entero y un booleano y que imprima un mensaje segun el tipo de 
dato de cada variable
"""
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de Texto"
    elif tipo == int:
        result = "Numero Entero"
    elif tipo == bool:
        result = "Booleano"
    
    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"este dato es del tipo: {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"

    return result

mi_lista = ["Hola Mundo", 77]
titulo = "Master in python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista,list))
print(comprobarTipado(titulo,str))
print(comprobarTipado(numero,int))
print(comprobarTipado(verdadero,bool))
