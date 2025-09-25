# El problema del vendedor viajero. Sea G un grafo de aristas ponderados cuyos nodos representen
# lugares geográficos. Sacar la ruta más corta posible que visite cada ciudad exactamente una sola
# vez y regrese a la ciudad de origen.

# Resulta que sacar la respuesta a fuerza bruta simple y sencillamente no es viable, ya que es un
# problema O(n!) y el factorial es una función que crece ridículamente rápido. Entonces, hay que
# encontrar una solución analítica; hasta ahora, la mejor solución que hay a ese problema es
# O(2n^3). Tampoco podemos revisar únicamente una muestra de los diferentes caminos, porque ¿qué
# tal si me salté una solución radicalmente mejor?

# Ante esto, vamos a pensar lateralmente y pensar: vamos a revisar una muestra, pero las muestras
# las vamos a tomar inteligentemente.

import numpy
import math


class Settings():
    def __init__(self):
        self.T_INICIAL = 100
        self.T_FINAL = 0

class Configuracion():

    campo = 0

    def __init__(self, C=None):
        if C is not None:
            self.campo = C.campo

    def alterar_tantito_campo(self, campo):
        pass

    def configuracion_cercana(self, C):
        Cprima = Configuracion(C)
        Cprima.alterar_tantito_campo()
        return Cprima

    def energia(self):
        return 0 # sacar una "energía"

def funcion_de_templado(T0, t):
    return T0 / (1+t)

settings = Settings()
C = Configuracion()
T = settings.T_INICIAL
t = 0
n = 1000

while True:
    for X in range(n):
        Cprima = C.configuracion_cercana()
        delta_E = Cprima.energia() - C.energia()
        # Pr(quedarnos con Cprima) -- función de Boltzmann
        q = math.e**(-delta_E / T)
        p = numpy.random.uniform(0, 1, 1)
        if p < q:
            C = Cprima
    t += 1
    T = funcion_de_templado(settings.T_INICIAL, t)
    if T < settings.T_FINAL:
        break


"""
# Algoritmo de alto nivel:
# Tomar una configuración inicial aleatoria C, poner temperatura inicial T y tomar t = 0
C = ConfiguracionInicial()
T = settings.T_INICIAL
t = 0

while True:
   for X in range(n):
      Cprima = C.configuracionCercana()
      delta_E = Cprima.energia() - C.energia()
      q = e ** (-delta_E / T)  # Pr(quedarnos con Cprima) -- función de Boltzmann
      p = numpy.random.uniform(0, 1, 1)
      if p < q:
         C = Cprima
   t += 1
   T = funcion_de_templado(T)
   if T < settings.T_FINAL:
      break

La "temperatura" se refiere a qué tan permisivo es el algoritmo para aceptar nuevas propuestas
de configuración. Una temperatura alta quiere decir que el algoritmo acepta cualquier cosa; una
temperatura baja hace que sea más estricto. Entonces, el chiste es comenzar con una "temperatura"
alta, y reducirla conforme a una función adecuada.

Teorema del templado: a través del teorema del límite central, se descubrió una serie de fórmulas
para decrementar la temperatura, que generalmente son fórmulas que decrecen rápido al principio
y lentamente al final (curva en forma de L)
T = T0 / (1+t)
T = T0 / Ln(1+t) - decrece más lentamente
T = k^t * T0 - decrece más rápido
T = T0 * (Tf/T0)^(t/n)
"""

# Problemas convexos: problemas matemáticos que tienen ciertas características que garantizan que
# sólo hay una solución.
