# se evalúa la condición, si es verdadera, se ejecuta el código dentro de while.

numero = 1
while numero < 100:
    print(numero)
    numero *= 2

# se crea una suerte de consola, donde itera hasta que se inserta por input la palabra salir.

# comando = ""

# while comando != "salir":
#     comando = input("$ ")
#     print(comando)

# para incluir cualquier forma de escritura en el input, usamos el método de string lower

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)


# loop infinito. esta aplicacion se va a ejecutar infinitamente y va a usar una cantidad de memoria
# infinita. si vamos a hacer uso de estos loops, hay que poner una condición de salida
comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
