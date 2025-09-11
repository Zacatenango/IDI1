import numpy

# 1: Generar una matriz Q de 5 x 5 con elementos aleatorios en [1, 10)
Q = numpy.reshape(numpy.random.uniform(1, 10, 25), (5,5), "C")

# 2: Sacar el promedio y tirar lo que esté por encima
Q_promedio = numpy.mean(Q)
porcentaje_arriba_promedio = numpy.mean(Q > Q_promedio) * 100
print(f"{porcentaje_arriba_promedio}% de los elementos de Q están por encima de su promedio")

# 3: Matriz L de 15x100 números reales en [0,8)
L = numpy.random.uniform(0,8, size=(15,100))

# 4: Arreglo M con los promedios de cada fila de L; tirar promedio de promedios
M = numpy.mean(L, axis=1)
promedio_M = numpy.mean(M)
print(f"El promedio de los promedios de L es {promedio_M}")



# 5: Simulación de lanzamiento de 2 dados
# Paso 1: posibles resultados y probabilidades
espacio_muestral = numpy.arange(2, 13)
probabilidades = numpy.array([1,2,3,4,5,6,5,4,3,2,1]) / 36

# Paso 2: tirar los dados 1000 veces
D = numpy.random.choice(espacio_muestral, size=1000, p=probabilidades)



# 6: Sacar 10 veces 3 canicas de una bolsa con 2 rojas, 3 azules y 5 blancas
bolsa_canicas = \
[
   "roja",
   "roja",
   "azul",
   "azul",
   "azul",
   "blanca",
   "blanca",
   "blanca",
   "blanca",
   "blanca",
]
resultaos = []
for X in range(10):
   resultaos.append(numpy.random.choice(bolsa_canicas, 3, replace=False))
print(f"Sacar 10 veces 3 canicas de una bolsa con 2 rojas, 3 azules y 5 blancas da: {resultaos}")
