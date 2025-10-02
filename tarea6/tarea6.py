import pandas
import numpy
import math
import json
import matplotlib.pyplot as pyplot

# Planteamiento del problema:
# Resolver con templado simulado el Problema del Vendedor Viajero con 8 
# ubicaciones, y la matriz de distancia en kilómetros ubicada en 
# probasSimAnn.xlsx, en la hoja "8c"
distancias = pandas.read_excel("probarSimAnn.xlsx", sheet_name="8c", index_col=0, nrows=9)
#print(f"{distancias}\n")

# Ajustes del programa, organizados en un diccionario de ajustes
SETTS = \
{
   "T_inicial": 1000,
   "T_final": 1,
   "n": 100
}

# Definimos una función de templado
def Ln(x):
   return numpy.log(x)
def func_templado(T0, t):
   #return T0 / (1+t)
   return T0 / Ln(1+t)



# Nuestra configuración estará encapsulada en una clase
class Configuracion():
   # Secuencia inicial al azar
   secuencia = [ "Tijuana", "Mérida", "GDL", "México", "León", "Monterrey", "Tapachula", "Chihuahua" ]
   # Secuencia óptima para probar, su distancia es 9524
   secuencia_optima = [ "Tijuana", "GDL", "León", "México", "Mérida", "Tapachula", "Monterrey", "Chihuahua" ]

   # Comienzo barajeando mi secuencia inicial
   def barajear_secuencia(self):
      self.secuencia = numpy.random.choice(self.secuencia, len(self.secuencia), replace=False).tolist()

   # Fórmula para sacar la "energía"
   def energia(self):
      distancia = 0
      for X in range(len(self.secuencia)):
         ciudad_actual = self.secuencia[X]
         ciudad_siguiente = self.secuencia[ (X+1)%len(self.secuencia) ]
         distancia += distancias[ciudad_actual][ciudad_siguiente]
      return distancia
   
   # Función para sacar una configuración cercana
   def sacar_configuracion_cercana(self):
      config_nueva = Configuracion()
      # Hay que asegurarnos de que la secuencia nueva sea una lista nueva y 
      # virgen, no una referencia a la anterior
      config_nueva.secuencia = self.secuencia.copy()
      indice_1 = numpy.random.randint(0, len(config_nueva.secuencia))
      indice_2 = numpy.random.randint(0, len(config_nueva.secuencia))
      # Intercambiamos 2 elementos al azar
      config_nueva.secuencia[indice_1], config_nueva.secuencia[indice_2] = \
         config_nueva.secuencia[indice_2], config_nueva.secuencia[indice_1]
      return config_nueva


# Ahora estoy listo para correr el templado simulado
T = SETTS["T_inicial"]
t = 0
n = SETTS["n"]
energias = []
iters = 0
C = Configuracion()
C.barajear_secuencia()


while T > SETTS["T_final"]:
   for X in range(n):
      Cprima = C.sacar_configuracion_cercana()
      delta_E = Cprima.energia() - C.energia()
      q = math.exp(-delta_E / T)
      p = numpy.random.random()
      if delta_E < 0 or p < q:
         C = Cprima
   t += 1
   T = func_templado(SETTS["T_inicial"], t)
   iters += 1
   energias.append(C.energia())

# Terminado el proceso, obtengo mi secuencia y saco su energía
print(f"La secuencia final es {json.dumps(C.secuencia)}")
print(f"Su distancia es {C.energia()}")
print(f"Iteraciones totales: {iters}")
pyplot.plot(energias)
pyplot.show()
