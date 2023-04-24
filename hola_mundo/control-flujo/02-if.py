# Se evalúa la condición entregada en el if. Si es true, se ejecuta la acción, si es false, no
# la indentación es muy importante en estos casos, sino, no funciona correctamente
edad = 22
if edad > 17:
    print("Puede ver la película")

print("Listo")

edad = 15
if edad > 17:
    print("Puede ver la película")

print("Listo")

edad = 15
if edad > 17:
    print("Puede ver la película")
else:
    print("No puedes entrar")
print("Listo")

# las evaluaciones se realizan de arriba hacia abajo, por lo que si la primera condición
# es true, las demás no se evalúan y se corta el flujo.

edad = 60
if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("No puedes entrar")
    print("Anda a otro lado")

print("Listo")


edad = 60
if edad > 65:
    print("Puede ver la película con superdescuento")
elif edad > 54:
    print("Puedes ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("No puedes entrar")
    print("Anda a otro lado")

print("Listo")
