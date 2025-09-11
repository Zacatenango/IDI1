import numpy

# 1. Sacar una lista L con los resultados de emular 1000 veces el experimento
# de obtener la suma de 2 dados, donde los dados están cargados y el 5 tiene
# doble probabilidad de salir por encima de los demás. ¿Qué porcentaje de los
# resultados fue 10?
espacio_muestral = numpy.arange(1,7)
probabilidades = numpy.array([1,1,1,1,2,1]) / 7
dado_1 = numpy.random.choice(espacio_muestral, size=1000, p=probabilidades)
dado_2 = numpy.random.choice(espacio_muestral, size=1000, p=probabilidades)
L = dado_1 + dado_2
L_10 = numpy.sum(L == 10) / 1000
print(f"1: {L_10}% de las tiradas dió 10")

# 2. Genere una lista M con los resultados de emular las respuestas aleatorias 
# de 1000 exámenes de 8 preguntas verdadero-falso.  ¿Cuál fue el promedio de 
# calificación sobre 100?
M = numpy.random.binomial(8, 0.5, 1000)
ej2_promedio = (numpy.mean(M) / 8) * 100
print(f"2: Calificación promedio: {ej2_promedio}")

# 3. Se sabe que por un crucero pasan en promedio 20 coches por minuto. Emule 
# aleatoriamente los resultados de tomar mediciones cada minuto durante una 
# hora. ¿Cuál fue el mayor y el menor valor obtenido?
ej3_carros_que_pasan_en_una_hora = numpy.random.poisson(20, 60)
ej3_maximo = ej3_carros_que_pasan_en_una_hora.max()
ej3_minimo = ej3_carros_que_pasan_en_una_hora.min()
print(f"3: Máximo: {ej3_maximo}, mínimo: {ej3_minimo}")

# 4. El coeficiente intelectual (IQ) es un estimador de la inteligencia general. 
# Se distribuye normalmente con una media de 100 y desviación estándar de 15.  
# Genere una lista Q que emule los IQ de una muestra aleatoria de 500 personas. 
# Si se considera a una persona superdotada si su IQ es igual o mayor a 130, 
# ¿cuántos superdotados se obtuvieron en la simulación?
Q = numpy.random.normal(100, 15, 500)
ej4_superdotados = numpy.sum(Q > 130)
print(f"4: Entre 500 personas, hay {ej4_superdotados} superdotados (IQ > 130)")