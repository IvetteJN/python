# funcion print, para imprimir

print("Hola mundo")

# para definir una función, usamos la palabra reservada def,
# luego el nombre que le asignamos a la función con paréntsis


def hola():
    print("Hola mundo!")
    print("Ultimate Python")


hola()

# si quisiéramos reutilizar una función como la de arriba, pero con la devolución
# de otro string, tenemos que cambiar el string, pero siempre nos va a devolver lo
# que escribamos en el print, por eso vamos a hacer uso de los parámetros de la función

# def hola():
#     print("Hola mundo!")
#     print("Bienvenida Ivette")

# hola()


def hola(nombre):  # usamos variable en la función, solo nos sirve en esta función(local)
    print("Hola mundo!")
    print(f"Bienvenida {nombre}")  # la variable acá es un parámetro


# aquí es obligatorio usar un valor para la variable indicada en la función
hola("Ivette")
hola("Chanchito feliz")

# a nombre en la declaración de la función: def hola(nombre) se le llama PARÁMETROS
# a nombre dentro de la función: print(f"Bienvenida {nombre}") se le llama PARÁMETRO DE LA FUNCIÓN
# a nombre en el llamado de la función: hola("Ivette")/hola("Chanchito feliz") se le llama ARGUMENTO

# si queremos que nuestra función tenga más de un parámetro:


def hola(nombre, apellido):
    print("Hola mundo!")
    print(f"Bienvenida {nombre} {apellido}")


hola("Ivette", "Nobiltá")
hola("Chanchito", "feliz")

# ARGUMENTOS OPCIONALES, si por ejemplo, no le pasamos un argumento a la función, le asignamos
# al parámetro un valor de defecto(se imprime si no le pasamos dicho argumento, de lo contrario,
# imprime el argumento)


def hola(nombre, apellido="Feliz"):
    print("Hola mundo!")
    print(f"Bienvenida {nombre} {apellido}")


hola("Ivette", "Nobiltá")
hola("Chanchito")
