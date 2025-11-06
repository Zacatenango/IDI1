# Parte 1: minimax estándar

class Nodo:
   def __init__(self, valor, izq=None, der=None):
      self.valor = valor
      self.izq = izq
      self.der = der


def minimax_ingenuo(nodo, profundidad, es_max):
   # Condición de salida: llegamos a la profundidad final o a una hoja
   if profundidad == 1 or (nodo.izq is None and nodo.der is None):
      return { "valor": nodo.valor, "nodo": nodo, "costado": None }
   
   # El nodo inicial es max: elegimos los hijos máximos
   if es_max:
      # Inicializamos nuestro valor máximo en una representación de Python del -infinito
      valor_max = float("-inf")
      mejor_hoja = None
      mejor_costado = None

      # Si hay nodo a la izquierda, llamamos recursivamente la función en ese nodo, con la 
      # profundidad decrementada; y ponemos que es Min, porque el hijo de un Max es Min.
      if nodo.izq is not None:
         resultao = minimax_ingenuo(nodo.izq, profundidad-1, es_max=False)
         # Terminando nuestra rama de recursividad, si nuestro valor es mayor que el 
         # valor máximo, ponemos eso en las variables del resultado e indicamos que el mejor costado
         # a seguir es el izquierdo
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "izquierdo"
      
      # Ahora, si hay nodo a la derecha, pasamos a revisarlo, igual con la profundidad decrementada
      # Y hacemos lo mismo que con el nodo izquierdo pero indicando que es a la derecha.
      if nodo.der is not None:
         resultao = minimax_ingenuo(nodo.der, profundidad-1, es_max=False)
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "derecho"
      
      # Terminada esta cadena de recursión, tiramos el resultado
      return { "valor": valor_max, "nodo": mejor_hoja, "costado": mejor_costado }
   
   # Ahora, si el nodo es min, hacemos lo mismo pero buscando un valor mínimo
   else:
      valor_min = float("inf")
      mejor_hoja = None
      mejor_costado = None

      if nodo.izq is not None:
         resultao = minimax_ingenuo(nodo.izq, profundidad-1, es_max=True)
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "izquierdo"
      if nodo.der is not None:
         resultao = minimax_ingenuo(nodo.der, profundidad-1, es_max=True)
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "derecho"
      return { "valor": valor_min, "nodo": mejor_hoja, "costado": mejor_costado }


# Aplicamos la función a un árbol de 4 niveles
raiz = Nodo(0)
raiz.izq = Nodo(4)
raiz.der = Nodo(9)
raiz.izq.izq = Nodo(5)
raiz.izq.der = Nodo(2)
raiz.der.izq = Nodo(1)
raiz.der.der = Nodo(-3)
raiz.izq.izq.izq = Nodo(7)
raiz.izq.izq.der = Nodo(3)
raiz.izq.der.izq = Nodo(4)
raiz.izq.der.der = Nodo(1)
raiz.der.izq.izq = Nodo(10)
raiz.der.izq.der = Nodo(2)
raiz.der.der.izq = Nodo(1)
raiz.der.der.der = Nodo(8)

print("----------------------------------- Parte 1: minimax ingenuo -----------------------------------")
resultao_max = minimax_ingenuo(raiz, 4, es_max=True)
resultao_min = minimax_ingenuo(raiz, 4, es_max=False)
print(f"Si la raíz es max, el valor final es {resultao_max['valor']}, la hoja es de valor {resultao_max['nodo'].valor}, y el costado es el {resultao_max['costado']}")
print(f"Si la raíz es min, el valor final es {resultao_min['valor']}, la hoja es de valor {resultao_min['nodo'].valor}, y el costado es el {resultao_min['costado']}")

resultao_max = minimax_ingenuo(raiz, 3, es_max=True)
resultao_min = minimax_ingenuo(raiz, 3, es_max=False)
print(f"3 niveles: si la raíz es max, el valor final es {resultao_max['valor']}, la hoja es de valor {resultao_max['nodo'].valor}, y el costado es el {resultao_max['costado']}")
print(f"3 niveles: si la raíz es min, el valor final es {resultao_min['valor']}, la hoja es de valor {resultao_min['nodo'].valor}, y el costado es el {resultao_min['costado']}")


# Parte 2: minimax con poda alfa-beta
class Nodo():
   def __init__(self, valor, izq=None, der=None):
      self.valor = valor
      self.izq = izq
      self.der = der


def minimax_poda_alfabeta(nodo, profundidad, alfa, beta, es_max, costado_raiz=None):

   # Condición de salida: llegamos a una hoja o a la profundidad final
   if nodo.valor is not None or profundidad == 0:
      return { "valor": nodo.valor, "nodo": nodo, "costado_raiz": costado_raiz }

   # El nodo es max: elegimos el hijo máximo igual que en minimax normal
   if es_max:
      valor_max = float("-inf")
      mejor_hoja = None
      mejor_costado = None

      if nodo.izq is not None:
         costado = costado_raiz if costado_raiz is not None else "izquierdo"
         resultao = minimax_poda_alfabeta(nodo.izq, profundidad-1, alfa, beta, es_max=False, costado_raiz=costado)
         
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = resultao["costado_raiz"]
         # Poda alfa-beta: alfa es igual a lo que sea mayor de entre la alfa existente y el valor max
         # Luego, si la beta es menor o igual a alfa, salgo de la función y con eso podo el subárbol
         # de la derecha
         alfa = max(alfa, valor_max)
         if beta <= alfa:
            return { "valor": valor_max, "nodo": mejor_hoja, "costado_raiz": mejor_costado }
      
      # No podé el costado derecho: lo evalúo
      if nodo.der is not None:
         costado = costado_raiz if costado_raiz is not None else "derecho"
         resultao = minimax_poda_alfabeta(nodo.der, profundidad-1, alfa, beta, es_max=False, costado_raiz=costado)
         
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = resultao["costado_raiz"]
         alfa = max(alfa, valor_max)
         # No reviso la beta porque ya no hay nada qué podar
      
      return { "valor": valor_max, "nodo": mejor_hoja, "costado_raiz": mejor_costado }
   
   # El nodo es min:
   else:
      valor_min = float("inf")
      mejor_hoja = None
      mejor_costado = None
      if nodo.izq is not None:
         costado = costado_raiz if costado_raiz is not None else "izquierdo"
         resultao = minimax_poda_alfabeta(nodo.izq, profundidad-1, alfa, beta, es_max=True, costado_raiz=costado)
         
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = resultao["costado_raiz"]
         # Poda alfa-beta: beta es igual a lo menor de entre la beta existente y el valor min
         # Si la beta es menor o igual a alfa, podo el subárbol de la derecha saliendo de la función
         beta = min(beta, valor_min)
         if beta <= alfa:
            return { "valor": valor_min, "nodo": mejor_hoja, "costado_raiz": mejor_costado }
      
      if nodo.der is not None:
         costado = costado_raiz if costado_raiz is not None else "derecho"
         resultao = minimax_poda_alfabeta(nodo.der, profundidad-1, alfa, beta, es_max=True, costado_raiz=costado)
         
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = resultao["costado_raiz"]
         beta = min(beta, valor_min)
         # No reviso la beta porque ya no hay nada qué podar

      return { "valor": valor_max, "nodo": mejor_hoja, "costado_raiz": mejor_costado }


# Ahora probamos
raiz = Nodo(0)
raiz.izq = Nodo(0)
raiz.der = Nodo(0)
raiz.izq.izq = Nodo(0)
raiz.izq.der = Nodo(0)
raiz.der.izq = Nodo(0)
raiz.der.der = Nodo(0)
raiz.izq.izq.izq = Nodo(3)
raiz.izq.izq.der = Nodo(5)
raiz.izq.der.izq = Nodo(6)
raiz.izq.der.der = Nodo(9)
raiz.der.izq.izq = Nodo(1)
raiz.der.izq.der = Nodo(2)
raiz.der.der.izq = Nodo(0)
raiz.der.der.der = Nodo(-1)


print("----------------------------------- Parte 2: minimax con poda alfa-beta -----------------------------------")
resultao_max = minimax_poda_alfabeta(raiz, 4, float("-inf"), float("inf"), es_max=True)
print(f"Si la raíz es max, el valor final es {resultao_max['valor']}, la hoja es de valor {resultao_max['nodo'].valor}, y el costado es el {resultao_max['costado_raiz']}")
