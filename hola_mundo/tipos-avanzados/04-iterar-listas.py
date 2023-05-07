# se pueden iterar listas, strings, el resultado de la función range, y lo hicimos con for
# entonces, vamos a iterar mascotas

mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# de esta manera iteramos todos los elementos de una lista:

# for mascota in mascotas:
#     print(mascota)

# si dentro de esta iteración quisiéramos acceder al índice del elemento que estamos iterando,
# podemos pasarle mascotas a una función que nos devuelva un iterable. enumerate.
# le pasamos como argumento, mascotas. enumerate devuelve tuplas (0, 'Pelusa) (1, 'Pulga), etc
# con esto, tenemos que desempaquetar tuplas. con for vamos a poder tomar el primer elemento (indice) y el segundo (nombre)
# así nos devolverá los índices con sus valores, pudiendo acceder a los índices

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
