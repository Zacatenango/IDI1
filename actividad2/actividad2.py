import numpy

# 1: Generar nuestras matrices
A = numpy.reshape(numpy.array([3,5,7,11]), (2,2))
B = numpy.reshape(numpy.array([-2, 4, 9, 10]), (2,2))
print(f"A = \n{A}")
print(f"B = \n{B}")

# 2: Sacar la matriz C = 3A + B + I2, donde I2 es una matriz identidad de 2 x 2
I2 = numpy.reshape(numpy.array([1, 0, 0, 1]), (2,2))
C = (3*A) + B - I2
print(f"C = \n{C}")

# 3: Concatenar en columnas las matrices A y B
D = numpy.concatenate((A, B), 1)
print(f"D = \n{D}")

# 4: Tirar la suma de los elementos de D y cuántos elementos pares tiene
suma_D = D.sum()
elementospares_D = (D % 2 == 0).sum()
print(f"Suma de D = {suma_D}")
print(f"Elementos pares de D = {elementospares_D}")

# 5: Sacar una matriz de 10 x 10 con los números naturales del 1 al 100 por columna
F = numpy.reshape(numpy.arange(100), (10,10), "F")
print(f"F = \n{F}")

# 6: Sacar la suma de los valores de F cuyos valores estén en el rango [10,20]
suma = F[:,1:3].sum()
print(f"Suma = {suma}")
