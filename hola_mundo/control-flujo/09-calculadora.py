# Crea una calculadora interactiva, donde interactuamos con la terminal
# hay numero? si no se ingresó numero, hay que indicarle al usuario que ingrese un numero, si ya
# hay un numero, le pedimos al usuario que ingrese una operación. Si no había ingresado un numero,
# pero ya lo ingresó, ahora le pedimos que ingrese una operación. ahora, ingrese otro numero
# y vamos a mostrar los resultados. a ese resultado ahora lo vamos a mostrar como el primer numero ingresado,
# sobre el cual haremos la siguiente operación, y asi sucesivamente.

# >>> Bienvenidos a la calculadora
# >>> Para salir escribí salir
# >>> Las operaciones son suma, multi, div y resta
# >>> Ingresa número: 12
# >>> Ingresa operación: suma
# >>> Ingresa siguiente número: 28
# >>> El resultado es 40
# >>> Ingresa operación: div
# >>> Ingresa siguiente número: 10
# >>> El resultado es 4.0
# >>> Ingresa operación: multi
# >>> Ingresa siguiente número: 5
# >>> El resultado es 20.0
# >>> Ingresa operación: resta
# >>> Ingresa siguiente número: 5
# >>> El resultado es 10.0
# >>> Ingresa operación: salir

print("Bienvenidos a la calculadora")
print("Para salir escribí salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
