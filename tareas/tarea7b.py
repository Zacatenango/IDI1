import pandas
import numpy
import math
import json
import matplotlib.pyplot as pyplot
import multiprocessing

# Planteamiento del problema:
# Resolver con templado simulado el Problema del Vendedor Viajero
distancias = pandas.read_excel("SA2.xlsx", sheet_name="54c_test", index_col=0, nrows=55)

# Ajustes del programa, organizados en un diccionario de ajustes
SETTS = \
{
   "T_inicial": 500,
   "T_final": 0.1,
   "n": 1000,
   "hilos": 4,
   "iteraciones": 4
}

# Definimos una función de templado
# (y un wrapper para el logaritmo natural porque log() no dice si es decimal o natural)
def Ln(x):
   return numpy.log(x)
def func_templado(T0, t):
   #return T0 / (1+t)
   #return T0 / Ln(1+t)
   return T0 * (0.95**t)

# Cargamos una vez nuestra configuración inicial desde el documento de Excel
secuencia_inicial = list(distancias.index)


# Nuestra configuración estará encapsulada en una clase
class Configuracion():
   secuencia = secuencia_inicial

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
# (es obligatorio recibir un parámetro en funciones paralelizadas)
def unhilo_templado_simulado(_):
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
      """ # Tope máximo de 5000 iteraciones
      if iters > 5000:
         break """
   
   return { "secuencia_final": C.secuencia, "distancia_final": C.energia(), "iteraciones": iters, "historial": historial_enfriamiento }


# Repito eso en paralelo, un cierto número de veces
# Por cómo funciona multiprocessing, aquí es obligatorio usar if __name__ == "__main__"
if __name__ == "__main__":
   for X in range(SETTS["iteraciones"]):
      with multiprocessing.Pool(processes=SETTS["hilos"]) as pool_de_hilos:
         resultaos = pool_de_hilos.map(unhilo_templado_simulado, range(SETTS["hilos"]))

      # Al terminar, saco el valor mínimo y la desviación estándar
      arr_distancias_finales = numpy.array([un_resultao["distancia_final"] for un_resultao in resultaos])
      desvstd = arr_distancias_finales.std()
      minimo = arr_distancias_finales.min()
      print(f"Iteración {X+1}/{SETTS['iteraciones']}: con {SETTS['hilos']} hilos, la distancia mínima es {minimo} y la desviación estándar es {desvstd}")

      # Diagnóstico: grafico un historial de enfriamiento
      #pyplot.plot(resultaos[0]["historial"])
      #pyplot.show()

      # Imprimo los resultados de cada hilo
      # (los resultados completos en un archivo)
      with open(f"resultaos_{X}.json", "w") as archivo_resultaos:
         json.dump(resultaos, archivo_resultaos)
      for un_resultao in resultaos:
         un_resultao.pop("historial")
         un_resultao.pop("secuencia_final")
         print(f"Un resultado de la iteración {X}: {json.dumps(un_resultao)}")
