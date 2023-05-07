numeros = [1, 2, 3]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

# para hacer lo mismo, de manera correcta:

numeros1 = [1, 2, 3]
primero, segundo, tercero = numeros1
print(primero, segundo, tercero)

# si solo queremos uno de los elementos, usando estas palabras:

numeros2 = [1, 2, 3]
primero, *otros = numeros2
print(primero)

# explicación:
# def n(*numeros):
# n(1, 2, 3)
# si usamos un for (iteración), nos va a empaquetar todos los elementos, menos el primero.

numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros = numeros3
print(primero, segundo)

numeros4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros, ultimo = numeros4
print(primero, ultimo)

numeros5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros, penu, ultimo = numeros5
print(primero, penu, ultimo)
