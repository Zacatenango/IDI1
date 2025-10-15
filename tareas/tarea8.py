import json


class Pila:
   def __init__(self, capacidad=100):
      self.data = []
      self.capacity = capacidad
   
   def push(self, dato):
      if len(self.data) < self.capacity:
         self.data.append(dato)
   
   def pop(self):
      return self.data.pop()

   def peek(self):
      return self.data[-1]

   def empty(self):
      return len(self.data) == 0
   
   def full(self):
      return len(self.data) == self.capacity
   
   def count(self):
      return len(self.data)
   
   def print(self):
      return json.dumps(self.data)


pila1 = Pila(50)
for X in range(1, 50, 2):
   pila1.push(X)
print(f"Stack: {pila1.print()}")


class Cola:
   def __init__(self, capacidad=100):
      self.data = []
      self.capacity = capacidad
   
   def enqueue(self, dato):
      self.data.insert(0, dato)
   
   def dequeue(self):
      return self.data.pop()

   def peek(self):
      return self.data[0]
   
   def empty(self):
      return len(self.data) == 0
   
   def full(self):
      return len(self.data) == self.capacity
   
   def count(self):
      return len(self.data)
   
   def print(self):
      return json.dumps(self.data)
   

cola1 = Cola(50)
while not pila1.empty():
   cola1.enqueue(pila1.pop())
print(f"Cola: {cola1.print()}")
print(f"Stack vacío: {pila1.print()}")

