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

# 3. Contestar 500 exámenes de 12 preguntas de 4 opciones múltiples, calificaciones sobre 100
examenes = numpy.random.binomial(12, 1/4, 500) * 100

# 4. En una fábrica se producen 10 pelotas en promedio por minuto. Sacar los resultados de tomar
# cuántas pelotas se producen por minuto en una hora del día. Sacar un arreglo N con el promedio
# diario de 30 días de mediciones de una hora. Sacar la desv std de los promedios
pelotas_porminuto_1h = numpy.random.poisson(10, 60)
N = numpy.random.poisson(10, (60,30))
N_promedios = N.mean(axis=0)
N_desvstd = N_promedios.std()

# 5. Una población mide 1.68 +- 0.14 m en promedio. Su distribución es normal. Sacar la estatura de
# 500 personas.
Q = numpy.random.normal(1.68, 0.14, 500)
Q_promedio = Q.mean()
Q_mayor = Q.max()
Q_min = Q.min()
print(f"Promedio: {Q_promedio}, mayor: {Q_mayor}, menor: {Q_min}")

