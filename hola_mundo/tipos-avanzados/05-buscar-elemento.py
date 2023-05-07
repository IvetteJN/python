# buscando elementos dentro de un arreglo.
# si queremos encontrar un elemento dentro de un listado, hacemos uso del método index

mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

print(mascotas.index("Pulga"))

# nos dice que es el elemento 1 de un arreglo
# pero si quisiéramos buscar un elemento que no existe en el arreglo?

# mascotas1 = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# print(mascotas1.index("Wolfgang"))

# python nos muestra error, en otros lenguajes nos devuelve -1. si no queremos un error, tenemos que controlar que el elemento exista en nuestro listado.
# Esto lo hacemos con un if

mascotas2 = ["Pelusa", "Pulga", "Felipe", "Wolfgang"]

if "Wolfgang" in mascotas2:
    print(mascotas2.index("Wolfgang"))

# si queremos contar cuántas veces existe un elemento en un arreglo, usamos el método count
# en la siguiente función, nos devuelve que "Wolfgang" se encuentra 2 veces, teniendo la primer ocurrencia en el índice 1.
# para tener un trabajo limpio, no deberían repetirse los elementos, y en esos casos deberíamos eliminar elementos (tema de la próxima clase)

mascotas3 = ["Pelusa", "Wolfgang", "Pulga", "Felipe", "Wolfgang"]

print(mascotas3.count("Wolfgang"))
if "Wolfgang" in mascotas2:
    print(mascotas3.index("Wolfgang"))
