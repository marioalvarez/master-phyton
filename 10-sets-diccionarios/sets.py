"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice, ni orden.
"""
personas = {
    "victor",
    "manolo",
    "Francisco"
}

personas.add("Freddy")
personas.remove("Francisco")
print(type(personas))
print(personas)