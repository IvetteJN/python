# En las siguientes funciones, ambas tienen una variable que se llama saludo,
# y ambas contienen valores distintos uno de otro. Cuando intentamos imprimir una de estas
# variables, nos da error. saludo is not defined en la segunda función.
# el alcance está determinado por el lugar donde se defina la variable.
# se puede llamar sólo desde donde se declara (variables locales)

# def saludar():
#     saludo = "Hola Mundo"


# def saludaChanchito():
#     saludo = "Hola Chanchito"


# print(saludo)

# entonces, a la variable saludo la definimos dos veces en cada función.
# serán variables completamente distintas e independientes

# def saludar():
#     saludo = "Hola Mundo"
#     print(saludo)

# def saludaChanchito():
#     saludo = "Hola Chanchito"
#     print(saludo)


# saludar()
# saludaChanchito()
# saludar()

# La definimos de forma global y será accedida de forma global
# debate que dice que la variable global es una mala práctica. NO USARLAS
# al llamarla de manera local, se le reasigna el valor.
saludo = "Hola Global"


def saludar():
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
print(saludo)  # estamos trabajando con la global
saludaChanchito()
saludar()

# si tenemos que trabajar con una variable global (no recomendable)

saludo = "Hola Global"


def saludar():
    global saludo  # asignamos el nombre de la variable global
    saludo = "Hola mundo"


print(saludo)
saludar()
print(saludo)

# ejemplo que da error por usar variables globales
# nos arroja que no se pueden concatenar dos strings (en saludo = "Hola Mundo", se cambia el valor
# del dato, ya no es más un entero sino que se convierte en string)

saludo = 24


def saludar():
    global saludo  # asignamos el nombre de la variable global
    saludo = "Hola mundo"


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
