nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python, 
este curso contempla todos los detalles
que necesitas aprender para encontrar
trabajo como programador
"""  # las comillas triples sirven para escribir texto de varias líneas

print(nombre_curso, descripcion_curso)

# len es utilizado para conocer la longitud del string
print(len(nombre_curso))
# accediendo al índice del valor de la variable
print(nombre_curso[0])
# recortamos, a la izquierda desde qué índice, a la derecha, hasta qué índice
print(nombre_curso[0:8])
# si no le indicamos un final, de default me toma el últio índice
print(nombre_curso[9:])
# si no le indicamos un principio, de default me toma el primer índice
print(nombre_curso[:8])
# no recorta el string
print(nombre_curso[:])
