# largo calcula la cantidad de caracteres de una cadena de caracteres, si bien esto lo podemos hacer
# con len, es para poner en práctica el depurador.

# def largo(texto):
#     resultado = 0 # inicializamos la variable en 0
#     for _ in texto: # agregamos un caracter por iteración
#         resultado += 1
#         return resultado # devolver el valor de resultado cuando llamemos la función, adrede está colocado dentro de la función


# l = largo("Hola Mundo")
# print(l)

# está función nos retorna el valor "1", que es incorrecto, ya que hola mundo tiene 10 caracteres

# pinchamos la pestaña de run & debug. create a launch.json file. python file. Nos crea un archivo json
# Para ejecutar el depurador, tenemos que crear un breakpoint para que el depurador se detenga y así analizar el trabajo
# creamos el print("chanchito") y colocamos el breakpoint en la línea (clic derecho del mouse en el número, create breakpoint)
# clic en play del debug. en variables, locals, function variables, largo:
# avanzamos una línea con el botón step over (flecha con puntito debajo), en esta línea no nos muestra nada, sólo nos dice lo que hará.
# pinchamos de nuevo y avanzamos a la siguiente línea. no ingresó a la función para mostrarnos el error. Pero en el panel tenemos el valor
# de l: 1, lo que nos demuestra que la función no está funcionando.
# stepover y debug detiene la depuración. No es la idea, presionamos nuevamente stepover para ir a la línea siguiente a la del breakpoint.
# stepinto. nos ingresa en la ejecución de la función (resultado = 0). en el panel vemos en variables locals, el valor texto: 'Hola Mundo'
# stepover. avanzamos a la siguiente línea, el for. En el panel, además del texto, vemos la variable local resultado = 0.
# stepover. todavía no ejecuta esta línea.
# stepover. nos lleva a la línea del return y ya podemos intuir por qué tenemos el error. entramos al for, me agrega el valor a la variable
# resultado e inmediatamente la retorna. y esto debería hacerlo al final de la ejecución del for.
# vemos en el panel que el primer valor de la variable _ es "H", por lo que la función lo ejecuta bien.
# stepover. salimos de la función porque nos lleva a print(l).
# Detenemos el debugger.


def largo(texto):
    resultado = 0  # inicializamos la variable en 0
    for _ in texto:  # agregamos un caracter por iteración
        resultado += 1
    return resultado  # Quitamos la indentación


print("chanchito")
l = largo("Hola Mundo")
print(l)

# corremos el debugger nuevamente con el play. nos ubica en el breakpoint
# stepover. nos lleva a la línea l = largo("Hola Mundo")
# stepinto. entramos en la función.
# stepover. línea for
# stepover. entramos a resultado += 1. y ya nos muestra en el panel el segundo caracter del string "o"
# stepover. nos suma otro caracter en la variable resultado: 2
# si seguimos así (stepover), vemos que la función ya se ejecuta como debe. detenemos el debugger con el cuadrado rojo
