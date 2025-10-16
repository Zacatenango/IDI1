# Los árboles son estructuras no indexadas; es decir, no hay un modo riguroso de asignarle un orden
# o índice.

# Los árboles son no lineales: si recorro aristas en línea recta, no recorreré toda la estructura.

# Rama: cualquier secuencia lineal dentro del árbol
# Rama principal: cualquier rama que vaya desde la raíz hasta una hoja
# Profundidad: la longitud de la rama principal más larga, siempre es de base 1
# Nivel: vértices que estén a la misma distancia de grafo de la raíz, puede ser de base 0
# Padre e hijo: 2 nodos conectados por un arista (en referencia al árbol genealógico)

# Árbol binario: árbol donde cada padre tiene máximo 2 hijos
# Arbol n-ario: árbol donde cada padre tiene máximo n hijos
# Árbol completo: árbol donde cada padre tiene todos los hijos posibles
# Árbol balanceado: árbol donde todas las hojas están en el mismo nivel

# El problema de la lectura: ¿cómo llego a un elemento específico en una estructura no indexada?
# Eso hace que sea más difícil buscar algo en un árbol. Para eso, se necesita llevar un registro de
# qué nodos han sido ya consultados. Los 2 algoritmos genéricos son depth-first y breadth-first.

# Búsqueda por profundidad:
# Se exprime el árbol rama principal por rama principal.
# Comenzamos por la derecha o izquierda (dirección principal, decisión personal pero debe ser 
# siempre constante)
# Al topar con una hoja, regresamos un nivel y nos vamos por el otro costado, y seguimos bajando por
# la dirección principal.
# Es más sencillo, pero ineficiente

# Búsqueda recursiva:
# Con una función que se re-llame a sí misma es posible buscar de forma bastante sencilla en un
# árbol binario. Es obligatorio tener una decisión de corte para que la función no se cicle.
# En árboles, la lógica es: re-llamar la función de buscar en un árbol sobre cada nodo, tomando
# en cuenta la propiedad de los árboles de que un subconjunto de los nodos del árbol es un sub-árbol
# cuya raíz es el nodo donde estoy buscando. La decisión de corte: si el nodo es una hoja, termino.
# Limitación: en las PCs de verdad, tienden a quedar muchas llamadas pendientes a función en el 
# call stack.

# Búsqueda por amplitud:
# Requiere una cola auxiliar.
# cola.enqueue(raiz)
# while elemento.valor != valor_buscado:
#    elemento = cola.dequeue()
#    cola.queue(elemento.hijo1)
#    cola.queue(elemento.hijo2)


class Nodo:
   def __init__(self, dato):
      self.dato = dato
      self.izq = None
      self.der = None
   
   def imprimir_P(self):
      if self.izq is not None:
         self.izq.imprimir_P()
      if self.der is not None:
         self.der.imprimir_P()
      print(self.dato)
   
   def impares_P(self):
      cuenta = 0
      if self.dato%2 == 1:
         cuenta += 1
      if self.izq is not None:
         cuenta += self.izq.impares_P()
      if self.der is not None:
         cuenta += self.der.impares_P()
      return cuenta


raiz = Nodo(2)
raiz.izq = Nodo(5)
raiz.der = Nodo(7)
raiz.izq.izq = Nodo(1)
raiz.izq.der = Nodo(4)
raiz.der.izq = Nodo(3)
raiz.der.der = Nodo(6)

raiz.imprimir_P()
print(f"Cuenta de impares: {raiz.impares_P()}")
