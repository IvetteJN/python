for j in range(3):  # outer for / outer loop
    for k in range(2):  # inner for / inner loop
        print(f"{j}, {k}")

# cuando ejecutamos el primer for, lee como condición el for en su línea de ejecución
# 0, 0 j = 0 y k = 0, porque es la inicialización del loop
# 0, 1 estamos en el segundo for por segunda vez, y en el primero seguimos por 1era vez. j = 0 y k = 1
# 1, 0 ya iteramos con los elementos de range del segundo for, volvemos al primero. j = 1 y k = 0
# 1, 1 j= 1 y k = 1
# 2, 0 j = 2 y k = 0
# 2, 1 j = 2 y k = 1
