# keywords arguments. Una manera de empaquetar todos los parámetros, pero en un sólo parámetro
# definimos la función, con parámetro precedido de dos asteriscos, esto nos permitirá
# trabajar con muchos parámetros, empaquetado en uno solo.

def get_product(**datos):
    print(datos)


# para 'llamar' el parámetro adecuadamente, tenemos que asignarle un nombre al
# argumento, por eso, id="id". En consola nos arrojará un diccionario {'id':'id'}
get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")

# para imprimir algunos datos de todos los pasados por argumento:


def get_product(**datos):
    print(datos["id"], datos["name"])
