mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]

# si quiero agregar un elemento en un índice determinado, uso el método insert, que necesita dos argumentos: índice y elemento a agregar
mascotas.insert(1, "Melvin")
# si quiero agregar un elemento al final del arreglo, puedo usar insert(-1,"valor a agregar"), pero la manera correcta es con append:
mascotas.append("Chanchito triste")

# para eliminar un elemento en particular, usamos remove y le pasamos como argumento el elemento a eliminar
# remove elimina sólo la primer ocurrencia del elemento que le pasamos como argumento. si tenemos más de una y queremos eliminar todas,
# tenemos que contar cuántas veces aparece ese elemento...
mascotas.remove("Pulga")
# para eliminar el último elemento usamos el método pop
mascotas.pop()
# si queremos eliminar un elemento en un índice particular usamos pop y le pasamos como argumento el índice
mascotas.pop(1)
# usamos la palabra reservada del, seguida del nombre de la lista con el índice del elemento que queremos eliminar
del mascotas[0]
# si queremos limpiar todo el arreglo, usamos el método clear
mascotas.clear()
print(mascotas)
