# Usando búsqueda por profunidad:
# Funciones que reciban el nodo raíz de un árbol, y tiren
# - El valor mínimo
# - La profundidad
# - Dado un número, sacar en qué nivel del árbol se encuentra
# - Tirar la cantidad de números pares
# - Tirar la cantidad de nodos

class Nodo:
   def __init__(self, dato):
      self.dato = dato
      self.izq = None
      self.der = None

def minimoP(nodo, minimo=None):
   minimo = nodo.dato
   if nodo.dato < minimo:
      minimo = nodo.dato
   if nodo.izq is not None:
      minimo = minimoP(nodo.izq, minimo)
   if nodo.der is not None:
      minimo = minimoP(nodo.der, minimo)
   return minimo

def cuentameP(nodo, numero):
   cuenta = 0
   if nodo.dato == numero:
      cuenta += 1
   if nodo.izq is not None:
      cuenta += cuentameP(nodo.izq, numero)
   if nodo.der is not None:
      cuenta += cuentameP(nodo.der, numero)
   return cuenta

def profundidadP(nodo, profundidad=0):
   profundidad += 1
   if nodo.izq is not None:
      profundidad = profundidadP(nodo.izq, profundidad)
   if nodo.der is not None:
      profundidad = profundidadP(nodo.der, profundidad)
   return profundidad

def paresP(nodo):
   cuenta = 0
   if nodo.dato%2 == 0:
      cuenta += 1
   if nodo.izq is not None:
      cuenta += paresP(nodo.izq)
   if nodo.der is not None:
      cuenta += paresP(nodo.der)
   return cuenta

raiz = Nodo(2)
raiz.izq = Nodo(5)
raiz.der = Nodo(7)
raiz.izq.izq = Nodo(1)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(3)
raiz.der.der = Nodo(6)
raiz.der.der.izq = Nodo(5000)

print(f"Valor mínimo: {minimoP(raiz)}")
print(f"Cuenta de un número 5: {cuentameP(raiz, 5)}")
print(f"Profundidad: {profundidadP(raiz)}")
print(f"Nodos pares: {paresP(raiz)}")

# Con búsqueda por amplitud, en un árbol binario con valores reales:
# - Cantidad de números nones
# - Valor máximo de los nodos
# - Dado un entero n, tirar todos los nodos del árbol por amplitud de los primeros n niveles
# - Dado un número, insertarlo en el árbol en la primera posición disponible dando prioridad a la derecha
# - Tirar la profundidad del árbol
