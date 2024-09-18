import random

# Crea una matriz de NxM con números aleatorios
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
for fila in matriz:
    print(fila)