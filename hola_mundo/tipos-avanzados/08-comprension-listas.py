# comprensión de listas
# si queremos, por ejemplo, tomar una lista con listas y obtener solo los nombres:

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# creamos una lista vacía e iteramos la lista original, filtrando solo los nombres y agregándolos a la lista vacía con append
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# map
# la operación de arriba, de manera correcta se hace de la siguiente manera:
# nombres = [expresion for item in items]
# entonces:
# nombres = [usuario[0] for usuario in usuarios]

# filter
# y si quisiéramos filtrar, le ponemos condición con if
# nombres = [expresion for item in items]
# entonces:
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# map y filter
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# ------------------------------------------------

# PROGRAMACIÓN FUNCIONAL: MAP Y FILTER
# map
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# print(nombres)

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
