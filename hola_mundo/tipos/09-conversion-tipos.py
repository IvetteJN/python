# x = input("")

# funciones nativas de python para conversión de tipos de datos
# no importa el tipo de dato que se ingrese en el input, será siempre de tipo string
# int() transforma el dato en integer
# str() transforma el dato en string
# float() transforma el dato en float
# bool() transforma el dato en boolean. bool toma cualquier dato y la evalua como true o false.
# truthy(true): con lo que no es falsy, es truthy
# falsy(false): string vacío(""), 0(cero), None(objeto)

print(bool(""))  # >>>False
print(bool("0"))  # >>>True
print(bool(None))  # >>>False
print(bool(" "))  # >>>True
print(bool(0))  # >>>False
