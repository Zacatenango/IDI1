import numpy



# La distribución binomial representa el desarrollo de un experimento de
# Bernoulli: un experimento aleatorio que sólo tiene 2 posibles resultados,
# donde la probabilidad de obtener 1 es constante y los resultados de los
# ensayos sucesivos son independientes. Clásicamente, los resultados son
# éxito y fracaso, pero también pueden llamarse True o False, "águila" o
# "sello", 1 o 0...

# 10 volados: experimento binomial hecho 10 veces con Pr(X=1) = 0.5
experimento_binomial = numpy.random.binomial(10, 0.5)



# Distribución de Poisson: representa experimentos donde se conoce el promedio
# de veces que ocurre algo, e.g. cuántas podría decir en una hora si dice un
# promedio de 100 muletillas por minuto
muletillas_de_Musk = numpy.random.poisson(100, 60)