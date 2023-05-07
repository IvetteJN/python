mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])  # para acceder a un elemento, lo hacemos de esta manera
mascotas[0] = "Bicho"  # para cambiar uno de los elementos
print(mascotas)
print(mascotas[0:3])  # para recibir un "rango" de elementos de la lista
# python considera por defecto, que el primer elemento es cero
print(mascotas[:3])
# python considera por defecto que tiene que devolver los elementos que restan de la lista
print(mascotas[2:])
# como a la izquierda del "0", no hay ningún elemento, va al final de la lista. en este caso, devuelve copito
print(mascotas[-1])
# devuelve los elementos pares de una lista. esto significa literalmente: toma el primer elemento, el siguiente saltalo, el siguiente tomalo, y asi sucesivamente.
print(mascotas[::2])
# devuelve los elementos impares de una lista. esto significa literalmente: toma el primer elemento, el siguiente saltalo, el siguiente tomalo, y asi sucesivamente.
print(mascotas[1::2])

# qué ocurriría si tengo más elementos? entonces, coloco así, para indicarle hasta cuánto queremos llegar de los elementos a seleccionar

numeros = list(range(1, 21))
print(numeros[::2])  # impares en ese rango
