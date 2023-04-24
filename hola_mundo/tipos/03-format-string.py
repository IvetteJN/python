nombre = "Ivette"
apellido = "Nobiltá"
# nombre_completo = nombre + " " + apellido

# para formatear un string, coloco las variables entre llaves,
# precedidas de la letra f. Concatena los strings. No importa el tipo de datos
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)

nombre_completo = f"{nombre[0]} {2 + 5}"
print(nombre_completo)
