# para ordenar de manera ascendente, usamos el método sort
numeros = [2, 4, 1, 45, 75, 22]
numeros.sort()
print(numeros)

# para ordenarlos al revés:
numeros1 = [2, 4, 1, 45, 75, 22]
numeros.sort(reverse=True)
print(numeros1)

# sorted. tenemos que pasarle como argumento el iterable que queremos ordenar, en este caso, numeros2.
# sorted devuelve una nueva lista, no afectando la lista anterior
numeros2 = [2, 4, 1, 45, 75, 22]
numeros3 = sorted(numeros2)
print(numeros2)
print(numeros3)

# si queremos cambiarle el orden, usamos reverse como antes:
numeros4 = [2, 4, 1, 45, 75, 22]
numeros5 = sorted(numeros4, reverse=True)
print(numeros4)
print(numeros5)

# si quisiéramos ordenar algo más complejo
usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]

usuarios.sort()
print(usuarios)

# pero si pusiéramos los índices al final? No los ordena
usuarios1 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios.sort()
print(usuarios1)

# sort solo ordena las listas si tenemos un elemento ordenable. en este caso, deberíamos pasarle un parámetro de ordenamiento al método sort

usuarios2 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios2)

# lambda o funciones anónimas. es mala práctica usar solo anónimas, pero si se usa una única vez, no está mal

usuarios3 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios3.sort(key=lambda el: el[1])
print(usuarios3)
