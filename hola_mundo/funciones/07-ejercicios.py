# desarrollar una función que reciba un texto y determine si es un palíndromo
# función para eliminar los espacios en blanco y función para que tome un texto y nos de un reverse.
# para ambas funciones usamos un for para iterar con cada uno de los caracteres

def no_space(texto):
    nuevo_texto = ""  # acá almacenaremos el nuevo valor de la nueva función. Comienza con un string vacío, vamos a recibir el string pasado por parámetro, lo vamos a iterar y lo vamos a concatenar, siempre y cuando no sea un string vacío
    for char in texto:  # por cada caracter en texto
        if char != " ":  # si char es distinto a un espacio
            # acá es donde va a concatenar cada uno de los caracteres, a menos que sea un string vacío
            nuevo_texto += char
    return nuevo_texto  # fuera del for, retornamos nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    # reemplazamos la variable de texto que recibimos como parámetro
    texto = no_space(texto)
    # aquí vamos a revertir los caracteres. pasamos texto(variable) como argumento en la función reverse
    texto_al_reves = reverse(texto)
    # cuando ejecutemos el script, deberíamos ver el string sin ningún espacio
    # acá comparamos para que nos devuelva true o false.incluimos el lower()
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("amo la paloma"))
print(es_palindromo("Hola Mundo"))

# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola Mundo", es_palindromo("Hola Mundo"))
