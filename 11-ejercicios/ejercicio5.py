"""
Ejercicio 5
crear una lista con el contenido de esta tabla:
Accion  Aventura  Deportes
GTA     Assains     Fifa 21
COD     Crash       Pro21
PUBG    prince of persia    Moto gp 21

Mostrar informacion ordenada
"""
tabla = [
    {
        "categoria":"accion",
        "juegos": ["Gta","Call of duty","Pubg"]
    },
    {
        "categoria":"Aventura",
        "juegos": ["Assasins","Clash Bandicoot","Prince of persia"]
    },
    {
        "categoria":"Deportes",
        "juegos": ["Fifa 21","Pes 21","Moto gp 21"]
    }
]

for categoria in tabla:
    print(f"------------------{categoria['categoria']}------")
    for juego in categoria['juegos']:
        print(juego)