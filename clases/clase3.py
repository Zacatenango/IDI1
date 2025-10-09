import numpy

numpy.random.seed(297974)
X = numpy.random.random(10)

# En la computadora no se pueden generar números sin órbita
# La tirada en la pseudoaleatoriedad es que la órbita sea gigante
# El tamaño de la órbita es básicamente cuántos números tienen que pasar
# para que la secuencia empiece a repetirse
X_medioGB = numpy.random.random(500000000)

# uniform(inicio,final,cantidad) genera flotantes desde el inicio hasta el 
# final, con distribución uniforme
uniforme = numpy.random.uniform(1,11,100)

# choice(arreglo, longitud) tira un arreglo con uno al azar de entre un arreglo
# Si le tiro replace=False como kwarg, cada elemento que salga se eliminará
# del arreglo (muestreo sin reemplazo)
# Si le tiro p=<arreglo de probabilidad>, rompo la probabilidad uniforme de
# que todos salgan.
# El arreglo p es un arreglo de distribución de probabilidad. Debe sumar 1,
# y p[X] indica la probabilidad de que arreglo[X] salga
vocales = ["a", "e", "i", "o", "u", "ypsilon" ]
dist_vocales = numpy.random.choice(vocales, 200, p=[0.5, 0.2, 0.2, 0.05, 0.04, 0.01])

# Se puede barajear un arreglo tirándole numpy.random.choice(arreglo, len(arreglo). replace=False)
uno_al_100 = range(100)
uno_al_100_barajeado = numpy.random.choice(uno_al_100, len(uno_al_100), replace=False)

# unique() saca los valores únicos de un arreglo
vocales_2 = numpy.unique(dist_vocales)

# Para sumar 2 vectores de números 
tiros_dados = numpy.random.randint(1, 7, (300000000,2))
tiros_dados_suma = numpy.sum(tiros_dados,1)

# Método de Box-Müller

