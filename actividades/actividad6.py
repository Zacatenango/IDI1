# Estructuras de datos lineales: podrían no estar indexadas (que cada elemento tiene su índice),
# pero sí están ordenadas. Ejemplos: lista ligada, stack, cola.
# Ejemplo: un parcero y pintador de paréntesis: el algoritmo es:
# - Encuentro un paréntesis de apertura: lo pusho a un stack
# - Encuentro un paréntesis de cierre: popeo el stack
# - Encuentro otra cosa: no hago nada
# Ejemplo: la notación RPN
# Ejemplo: en finanzas, el span de las acciones de una empresa se sacan con un stack

# Colas FIFO, stacks LIFO
# Stack: push con .append(), pop con .pop(), peek con [-1]
class Pila():
   def __init__(self):
      self.datos = list()
   
   def pushar(self, X):
      self.datos.append(X)
   
   def popear(self):
      return self.datos.pop()

   def picar(self):
      return self.datos[-1]

pilita = Pila()
pilita.push(3)
pilita.push(5)
pilita.push(10)
pilita.push(15)
valor = pilita.pop()
valor2 = pilita.picar()



# Cola: enqueue con 


