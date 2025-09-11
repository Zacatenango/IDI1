import numpy

# 1: Inicializar la semilla de pseudoaleatoriedad
numpy.random.seed(297974)

# 2: Generar un arreglo G con elementos [3, 6, 9, ..., 39]
G = numpy.array(range(3, 40, 3))

# 3: Barajear G
G = numpy.random.choice(G, len(G), replace=False)

# 4: Sacar un arreglo H con 4 elementos de G 