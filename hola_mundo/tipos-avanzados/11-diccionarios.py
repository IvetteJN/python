# los diccionarios se escriben entre {}. cada llave tiene que ser un string y tienen que estar separadas por comas. los valores de cada llave pueden ser cualquier cosa

punto = {"x": 25, "y": 50}
print(punto)
# para acceder a una de las llaves, tenemos que poner el nombre de la llave
print(punto["x"])
print(punto["y"])

# podemos crear llaves a los diccionarios de esta manera:
punto["z"] = 45
print(punto)

# para acceder a una llave dentro de un diccionario, pero que no existe:
# print(punto, punto["lalaland"])

# entonces, deberíamos preguntar:
if "lala" in punto:
    print("encontré lala", punto["lalaland"])

# o podemos:
print(punto.get("x"))

# por ejemplo, si la llave no existe, nos devolverá "None"
print(punto.get("lalaland"))

# y si quisiéramos que nos arroje un mensaje en el caso de no encontrar la llave:
print(punto.get("lalaland", 97))

# si quisiera eliminar un valor de una llave y su llave, uso del
del punto["x"]
print(punto)

# también puedo eliminar una llave de un diccionario:
del (punto["y"])
print(punto)

# se pueden iterar las llaves de un diccionario con un for:

punto2 = {"x": 25, "y": 53, "z": 38}
for valor in punto2:
    print(valor)

# para iterar los valores de las llaves de un diccionario:

punto2 = {"x": 25, "y": 53, "z": 38}
for valor in punto2:
    print(valor, punto2[valor])

# para poder acceder a los elementos de un diccionario, puedo también, nos devolverá una tupla:
punto2 = {"x": 25, "y": 53, "z": 38}
for valor in punto2.items():
    print(valor)

# y podremos desempaquetar:
for llave, valor in punto2.items():
    print(llave, valor)

#
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Ivette"},
    {"id": 4, "nombre": "Felipe"},
]

# para acceder a los nombres:

for usuario in usuarios:
    print(usuario["nombre"])
