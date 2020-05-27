"""
ejercicio 10
pedir por pantalla la nota de 15 alunnos y sacar por pantalla
cuanto han aprovado y cuantos han repetido
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"ingresa la nota del alunmo {contador}: "))

    if nota >= 5:
        aprobados+= 1
    else:
        suspendidos += 1
    contador += 1

print(f"alumnos aprobados: {aprobados}, alumnos suspendidos: {suspendidos}")