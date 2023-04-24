n1 = input("Ingresa primer número")
n2 = input("Ingresa segundo número")

print(n1, n2)

# Para realizar cálculos con los datos ingresados,
# debo transformar los datos (string) a números, de lo contrario:
# print(n1 + n2) >>> n1n2

n1 = int(n1)
n2 = int(n2)

print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicación es {multi}.
El resultado de la división es {div}.
"""

print(mensaje)
