def suma(a, b):
    print(a + b)


suma(2, 5)


# def suma(a, b, c):
#     print(a + b + c)


# suma(2, 5, 7)

# si cada vez que quiero reutilizar una función, tengo que cambiar la cantidad de argumentos,
# utilizaremos una nueva instrucción. Parámetros con *, iterables

def suma(*numeros):  # en este caso, numeros será un iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)  # indentación!!!!


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)  # todos estos son iterables, lo que nos permite usar el for
