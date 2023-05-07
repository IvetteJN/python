# creamos una tupla, son iguales a las listas PERO no se pueden modificar, no se pueden agregar, eliminar o modificar elementos
# si podemos crear una nueva lista o una nueva tupla a partir de una tupla ya existente
# las usamos cuando no queremos modificar "accidentalmente" algún elemento que se encuentre dentro de un listado

numeros = (1, 2, 3)
print(numeros)

# podemos concatenar tuplas para crear una nueva tupla
numeros1 = (1, 2, 3) + (4, 5, 6)
print(numeros1)

# se pueden crear a partir de listas, con la función tuple, que recibe cualquier tipo de dato que sea iterable (podemos pasarle también strings por ejemplo)
punto = tuple([1, 2])
print(punto)

# no podemos usar ni pop ni append, nos arrojará error:
numeros.pop()

# si podemos acceder a los elementos de la tupla de esta manera, ya que nos crea una nueva tupla, asignada a la nueva variable "menosNumeros"
menosNumeros = numeros[:2]
print(menosNumeros)

# también desempaquetarlas:
primero, segundo, *otros = numeros

# podemos iterarlas:
for n in numeros:
    print(n)

# si intentamos modificarla, accediendo al primer elemento otro valor, nos da error:
numeros[0] = 5

# si tuviéramos que modificarla, creamos una nueva variable "listaNumeros" y modificamos el primer elemento de la lista, pero no la tupla
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)
