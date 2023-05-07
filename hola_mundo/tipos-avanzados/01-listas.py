# creamos una variable llamada numeros, tenemos el signo igual que significa que lo de la
# derecha se lo estamos asignando a la variable.
# entre corchetes colocamos los elementos de la lista.

numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["chanchito", "feliz"]
palabrasFelices = ["chanchito", "feliz", "Felipe", "alumno"]
booleans = [True, False, True, True]
matriz = [[0, 1], [1, 0]]

print(numeros, letras, palabras, palabrasFelices, booleans, matriz)

# ceros = [0,0,0,0,0,0,0] # para hacer una lista con caracteres repititivos, podemos hacerlo de la siguiente forma:
ceros = [0] * 10
print(ceros)

ceros_y_unos = [0, 1] * 10
print(ceros_y_unos)

# para crear una lista maestra que reuna diversos valores

numeros = [1, 2, 3]
letras = ["a", "b", "c"]
alfanumerico = numeros + letras
print(alfanumerico)

# un listado con un rango de números

rango_default = list(range(10))  # devuelve 10 números, del 0 al 9
# si queremos que la lista tenga del 1 al 10, le pasamos como parámetro a range, el rango de números que queremos que contenga
rango = list(range(1, 11))
print(rango, rango_default)

# lista de string
chars = list("hola mundo")
print(chars)
