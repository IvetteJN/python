# loop for sirve para iterar una lista de elementos. Por ejemplo, tenemos una lista
# de usuarios, y cada usuario tiene un nombre y un apellido. Y queremos crear un campo
# nuevo con el nombre completo, para eso vamos a crear con el for ese campo.
# También se usa para buscar elementos.
# Operaciones matemáticas.

# usamos la palabra reservada for, luego declaramos una variable(numero),
# más la palabra reservada in, por último la reservada range(), que nos crea
# una secuencia. La variable va cambiando a medida que se itera el range.
# numero va a valer 0, después 1, 2, 3 y por último 4

for numero in range(5):
    print(numero)

# Operación matemática

for numero in range(5):
    print(numero, numero * 'Hola Mundo')


# buscar elementos. cuando queremos cortar la iteración una vez encontrado el
# elemento, usamos la reservada break

buscar = 3
for numero in range(5):
    if numero == buscar:
        print("encontrado", buscar)
        break

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break

buscar = 10
for numero in range(5):
    if numero == buscar:
        print("encontrado", buscar)
        break
# for else
else:
    print("No encontré el número buscado")

# range(5) es un iterable, cualquier cosa con la que podamos iterar.
# usuario

# for usuario in usuarios:
#   usuario.id

# iterables: listas, tuplas, strings

for char in "Ultimate Python":
    print(char)
