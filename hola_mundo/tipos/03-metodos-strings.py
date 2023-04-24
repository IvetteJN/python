# los métodos son funciones que se encuentran dentro de un objeto
# por ejemplo, upper es método de animal

animal = " chanCHito feliz "
# mayúscula
print(animal.upper())
# minúscula
print(animal.lower())
# la primer letra en mayúscula y lo demás en minúscula
print(animal.capitalize())
# toma la primer letra de cada palabra y la pone en mayúscula, para convertirlo en un título
print(animal.title())
# quita los espacios innecesarios
# si usamos strip y capitalize, necesariamente capitalize debe estar después de strip,
# ya que de lo contrario cuenta el espacio inicial y no cambiala primer letra a mayúscula, de ser necesario
print(animal.strip())
# otra forma de resolver lo arriba descripto, es uniendo métodos
print(animal.strip().capitalize())
# quita el espacio de la izquierda
print(animal.lstrip())
# quita los espacios de la derecha
print(animal.rstrip())
# me devuelve el índice del caracter indicado
print(animal.find("ch"))
# si le indicamos un caracter que no existe, nos devuelve -1
print(animal.find("cH"))
# necesariamente lleva dos argumentos. indicamos con qué caracteres queremos
# reemplazar, si no encuentra la cadena de caracteres, no cambiará nada
print(animal.replace("nCH", "j"))
# find devuelve el índice que le pertenece a los caracteres indicados, in devuelve un boolean
print("nCH" in animal)
# si queremos saber si NO se encuentran los caracteres dentro del string
print("nCH" not in animal)
