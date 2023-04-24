# and, or, not

# and: si se cumplen dos condiciones, por ejemplo x > 5 and y > 10. si por
# alguna razón, uno de los valores no es true, la condición completa es false.

# or: si una de las dos condiciones se cumplen, por ejemplo x > 5 or y > 10. Si
# una de las dos es true, la condición completa es true. Si ambos son false, la
# evaluación total es false

# not: niega el resultado de una operación

gas = True
encendido = True

if gas and encendido:
    print("Puedes avanzar0")

gas = False
encendido = True

if gas and encendido:
    print("Puedes avanzar1")

gas = False
encendido = True

if gas or encendido:
    print("Puedes avanzar2")

gas = False
encendido = False

if gas or encendido:
    print("Puedes avanzar3")

gas = False
encendido = False

if not gas or encendido:
    print("Puedes avanzar4")

gas = False
encendido = False
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar5")

gas = True
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar6")

gas = True
encendido = True
edad = 18

if gas and (encendido or edad > 17):
    print("Puedes avanzar7")

gas = False
encendido = True
edad = 18

if gas and (encendido or edad > 17):
    print("Puedes avanzar8")

gas = True
encendido = True
edad = 18

if not gas and (encendido or edad > 17):
    print("Puedes avanzar9")

# operadores de cortocircuito, como por ejemplo, si usamos el and, todas las evaluaciones
# deben ser true. Pero si la primera es false, la segunda no la evalúa.
# Sirven para ahorrar trabajo de cómputo. Se evalúa todo de izquierda a derecha.
# Si hay paréntesis, se evalúa primero eso y después todo lo demas.
# En el caso del or, se evalúa el primero y si es true, no lee la de la derecha.
# y si el primero es false, se evalúa necesariamente el de la derecha.
gas = True
encendido = True
edad = 18

if not gas and encendido and edad > 17:
    print("Puedes avanzar10")

gas = False
encendido = True
edad = 18

if not gas and encendido or edad > 17:
    print("Puedes avanzar10")
