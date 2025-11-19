import numpy

# Lista L con los primeros 50 números naturales nones
L = [X for X in range(50) if (X % 2) == 0]

# Arreglo A a partir de la lista L
A = numpy.array(L)

# Imprimir el séptimo item de A, las posiciones 3-9, y los últimos 3 en orden descendente
print(f"Séptimo item de A: {A[7]}; Posiciones 3-9: {A[3:10]}; Últimos 3 en orden descendente: {A[-1:-3]}")

# Arreglo B del 20 al 5, de 3 en 3
B = numpy.array(range(20, 5, 3))

# C = arreglo B volteado
C = B[::-1]

# Arreglo D de 100 números del 2 al 30
D = numpy.linspace(2, 30, 100)

# Tirar el tamaño del paso
print(f"Tamaño de paso para generar D: {D[1] - D[0]}")

# E = 100 números del 5 al 100, de tipo entero
E = numpy.linspace(5, 100, 100, dtype="int")

# I = elmeentos de A que sean múltiplos de 3
I = A[ (A % 3 == 0) ]

# F = elementos de D tomados por filas (estilo C) en matriz de 10 x 10
F = numpy.reshape(D, (10,10), "C")

# G = idem, pero por columnas (estilo Fortran)
G = numpy.reshape(D, (10,10), "F")

# M = elementos de G de las filas 1 y 2, columnas 3-6
M = G[0:2, 2:6]

# N = elementos de G al cuadrado, menos 3
N = (G**2) - 3

# Tirar "SI" si algún elemento de N es divisible entre 17, "NO" de lo contrario
print("SI" if numpy.any(N % 17 == 0) else "NO")

# Tirar tercera fila de F, y cuarta columna de G
print(f"{F[2]}, {G[:,3]}")

# H = F + G
H = F + G

# Cambiar los elementos de H menores de 30 por ceros y guardar la matriz resultante en K
H[H<30] = 0
K = H

# Tirar la cantidad de columnas de K cuya suma sea mayor de 500

