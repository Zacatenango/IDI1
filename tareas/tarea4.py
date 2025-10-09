import numpy

# 1. Sacar el resultado de tirar 1000 veces 2d8 siendo las caras 1, 2, 2, 3, 4, 6, 10 y 12.
caras = [1, 2, 2, 3, 4, 6, 10, 12]
tiradas = numpy.random.choice(caras, size=(1000, 2))
L = tiradas.sum(axis=1)
valores, cuenta = numpy.unique(L, return_counts=True)
moda = valores[numpy.argmax(cuenta)]
menos_frecuente = valores[numpy.argmin(cuenta)]

# 2. Repartir 5000 veces 5 cartas de una baraja de 4 colores del 1 al 10
baraja = numpy.tile(numpy.arange(1, 11), 4)
