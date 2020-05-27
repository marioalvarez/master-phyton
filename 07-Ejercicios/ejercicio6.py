"""
ejercicio 6
mostrar todas la tablas de multiplicar del 1 al 10
    -mostrar el titulo de la tabla
    -mostrar la las multiplicaciones de la tabla
"""

for cabecera in range(1,11):
    print("#### #### #### #### #")
    print(f"### tabla del {cabecera} ###")
    print("#### #### #### #### #")

    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")

