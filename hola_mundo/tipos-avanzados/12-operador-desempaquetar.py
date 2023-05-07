# tenemos una lista, y podemos imprimirla así: print(lista), pero si quisiéramos que cada valor
# de la lista fuera asignado a un argumento de la lista, pongo print(1, 2, 3, 4), entonces el valor 1 se asigna al argumento 1 y así sucesivamente

lista = [1, 2, 3, 4]
print(1, 2, 3, 4)  # esto mismo se puede hacer con
print(*lista)  # el operador de desempaquetamiento

# también con las tuplas:
tupla = (1, 2, 3, 4)
print(1, 2, 3, 4)
print(*tupla)

# en el caso que tuviéramos una función, y los 3 argumentos los tuviéramos dentro de una lista,
# llamaríamos esta función, pasándole como argumento nuestra lista con el operador de desempaquetamiento
# para que se asignara a cada uno de los argumentos:

# def n(n1, n2, n3):

# también se pueden combinar listas:
lista2 = [5, 6]

combinada = [*lista, *lista2]
print(combinada)

# se pueden agregar elementos
combinada2 = ["Hola", *lista, "Mundo", *lista2, "chanchito"]
print(combinada2)

# también se pueden utilizar con los diccionarios:
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

# si tuviéramos una llave en el punto3 y a su vez, la misma en el punto4, me borra la llave del primer conjunto.
# la manera de asignar propiedades es de derecha a izquierda.
punto3 = {"x": 19, "y": "hola"}
punto4 = {"y": 15}

nuevoPunto2 = {**punto3, **punto4}
print(nuevoPunto2)

# agregar más valores a un diccionario, en cualquier lugar del mismo

punto3 = {"x": 19, "y": "hola"}
punto4 = {"y": 15}

nuevoPunto2 = {**punto3, "lala": "hola mundo", **punto4, "z": "mundo"}
print(nuevoPunto2)
