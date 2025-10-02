import pandas
import numpy
import math
import json
import matplotlib.pyplot as pyplot

# Planteamiento del problema:
# Resolver con templado simulado el Problema del Vendedor Viajero con 820
# ubicaciones, y la matriz de distancia en kilómetros ubicada en 
# 20_ubicaciones.xlsx, en la hoja 20c_test
distancias = pandas.read_excel("20_ubicaciones.xlsx", sheet_name="20c_test", index_col=0, nrows=21)
#print(f"{distancias}\n")

# Ajustes del programa, organizados en un diccionario de ajustes
SETTS = \
{
   "T_inicial": 10000,
   "T_final": 1,
   "n": 100
}

# Definimos una función de templado
# (y un wrapper para el logaritmo natural porque log() no dice si es decimal o natural)
def Ln(x):
   return numpy.log(x)
def func_templado(T0, t):
   return T0 / (1+t)
   #return T0 / Ln(1+t)
   #return T0 * (0.95**t)



# Nuestra configuración estará encapsulada en una clase
class Configuracion():
   secuencia = \
   [
      "Acatic",
      "Acatlán de Juárez",
      "Ahualulco de Mercado",
      "Ahuatlán",
      "Ahuisculco",
      "Ajijic",
      "Alista",
      "Allende",
      "Altus Bosques",
      "Amacueca",
      "Amatitán",
      "Ameca",
      "Antonio Escobedo",
      "Arandas",
      "Atacco",
      "Atemajac de Brizuela",
      "Atengo",
      "Atenguillo",
      "Atequiza",
      "Atotonilco el Alto",
   ]

   def barajear_secuencia(self):
      self.secuencia = numpy.random.choice(self.secuencia, len(self.secuencia), replace=False).tolist()

   def energia(self):
      distancia = 0
      for X in range(len(self.secuencia)):
         ciudad_actual = self.secuencia[X]
         ciudad_siguiente = self.secuencia[ (X+1)%len(self.secuencia) ]
         distancia += distancias[ciudad_actual][ciudad_siguiente]
      return distancia
   
   def sacar_configuracion_cercana(self):
      config_nueva = Configuracion()
      config_nueva.secuencia = self.secuencia.copy()
      indice_1 = numpy.random.randint(0, len(config_nueva.secuencia))
      indice_2 = numpy.random.randint(0, len(config_nueva.secuencia))
      config_nueva.secuencia[indice_1], config_nueva.secuencia[indice_2] = \
         config_nueva.secuencia[indice_2], config_nueva.secuencia[indice_1]
      return config_nueva


# Ahora estoy listo para correr el templado simulado
def unhilo_templado_simulado():
   T = SETTS["T_inicial"]
   t = 0
   n = SETTS["n"]
   historial_enfriamiento = []
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
      historial_enfriamiento.append(C.energia())
      if (iters % 100 == 0):
         print(f"Van {iters} iteraciones...")
      # Tope máximo de 5000 iteraciones
      if iters > 5000:
         break
   
   return { "secuencia_final": C.secuencia, "distancia_final": C.energia(), "iteraciones": iters, "historial": historial_enfriamiento }

resultaos = [ unhilo_templado_simulado() ]

# Al terminar, saco el valor mínimo y la desviación estándar
arr_distancias_finales = numpy.array([un_resultao["distancia_final"] for un_resultao in resultaos])
desvstd = arr_distancias_finales.std()
minimo = arr_distancias_finales.min()
print(f"Repetido 22 veces, la distancia mínima es {minimo} y la desviación estándar es {desvstd}")
