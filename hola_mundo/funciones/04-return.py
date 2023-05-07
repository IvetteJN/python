def suma(a, b):
    resultado = a + b
    print(resultado)


suma(1, 2)

# si yo quiero obtener el resultado y asignarlo a una variable para poder utilizarlo
# más adelante, como por ejemplo en la función de suma, uso return


def suma(a, b):
    # variable resultado
    resultado = a + b
    return resultado


# creo una nueva variable
c = suma(1, 2)
d = suma(c, 2)

print(d)
