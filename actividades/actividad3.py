import numpy

# 1: Inicializar la semilla de pseudoaleatoriedad
numpy.random.seed(297974)

# 2: Generar un arreglo G con elementos [3, 6, 9, ..., 39]
G = numpy.array(range(3, 40, 3))

# 3: Barajear G
G_barajeado = numpy.random.choice(G, len(G), replace=False)

# 4: Sacar un arreglo H con 4 elementos de G seleccionados al azar sin reemplazo
H = numpy.random.choice(G, 4, replace=False)

# 5: Tirar un arreglo L de 100 números aleatorios enteros en [5, 100]
L = numpy.random.randint(5, 101, 100)

# 6: Tirar la cantidad de números pares en L
L_pares = numpy.sum(L % 2 == 0)

# 7: Arreglo M de 100 números aleatorios en [3,10)
M = numpy.random.uniform(3, 10, 100)

# 8: Tirar la suma de los elementos de M que están en [5,8]
M_suma = numpy.sum( M[(M>=5) & (M<=8)] )