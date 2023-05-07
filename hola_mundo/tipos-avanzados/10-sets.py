# set significa grupo o conjunto. colección de datos que no se puede repetir
# por ejemplo, en el siguiente set tenemos elementos repetidos, nos va a imprimir los datos, una sola vez
# remueve los duplicados.

primer = {1, 1, 2, 2, 3, 4}
print(primer)

# se pueden trabajar muy similar a las listas:
primer1 = {1, 1, 2, 2, 3, 4}
primer1.add(5)
primer1.remove(1)
print(primer1)

# transformamos segundo (lista) en un set. usamos la función set, que recibe un iterable(como justamente lo son las listas)
primer2 = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)

# operador de los sets | nos combina ambos sets, sin repetir. el operador se llama UNIÓN
primer3 = {1, 1, 2, 2, 3, 4}
segundo1 = [3, 4, 5]
segundo1 = set(segundo1)
print(primer3 | segundo1)

# operador intersección & nos devuelve los elementos que se encuentren tanto en el primer set como en el segundo
primer4 = {1, 1, 2, 2, 3, 4}
segundo2 = [3, 4, 5]
segundo2 = set(segundo2)
print(primer4 & segundo2)

# operador de diferencia - . nos muestra los datos que se encuentran en el primer conjunto(izquierda)
# pero que además le estamos quitando los que se encuentran a la derecha: 1, 1, 2, 2, 3, 4 - 3, 4, 5 = 1, 2
# calcula la diferencia entre dos sets. (REVISAR, NO LO ENTIENDO MUY BIEN)
primer5 = {1, 1, 2, 2, 3, 4}
segundo3 = [3, 4, 5]
segundo3 = set(segundo3)
print(primer5 - segundo3)

# diferencia simétrica ^ . nos devuelve los elementos que se encuentren en el primer y segundo conjunto, pero que no se encuentren en ambos.

primer6 = {1, 1, 2, 2, 3, 4}
segundo4 = [3, 4, 5]
segundo4 = set(segundo4)
print(primer6 ^ segundo4)

# los sets no se encuentran ordenados y nosotros no podemos acceder a los elementos que contiene
# segundo[0]
# pero si podemos:
segundo4 = [3, 4, 5]
if 5 in segundo4:
    print("Hola mundo")
