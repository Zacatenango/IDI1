import math
import numpy as np

rng = np.random.default_rng()

# Utilice el método de Montecarlo para obtener la probabilidad estimada de triunfo para el juego 
# "Aguja de Buffon". Sea L la longitud de la aguja y D la distancia entre líneas. Use N = 100,000
# experimentos.
N = 100000
D = 1

def experimento_buffon(L, D):
   x = rng.uniform(0, D / 2)
   theta = rng.uniform(0, math.pi / 2)
   media_proyeccion = (L / 2) * math.sin(theta)
   return media_proyeccion >= x

def Pr(L, D, N):
   triunfos = 0
   for X in range(N):
      if experimento_buffon(L, D):
         triunfos += 1
   return triunfos / N

def estimar_pi(P):
   return 2.0 / P


# Caso 1: L = D
# Observamos que sí nos da una aproximación al valor de pi como resultado.
L = D
Pr_exito_caso1 = Pr(L, D, N)
pi_estimado = 2 / Pr_exito_caso1
print(f"Experimentos N = {N}")
print("Caso L = D:")
print(f"  Longitud L = {L}, Separacion D = {D}")
print(f"  Probabilidad estimada P = {Pr_exito_caso1:.6f}")
print(f"  Valor teórico de 2/pi = {2/math.pi:.6f}")
print(f"  Estimacion de pi desde P = {pi_estimado:.6f}")


# Caso 2: L = D/2
# Observamos que dividir la distancia entre líneas nos multiplica la estimación
# de pi que obtenemos como resultado: dividimos entre 2, nuestro resultado es
# prácticamente 2*pi.
L = D / 2
Pr_exito_caso2 = Pr(L, D, N)
pi_estimado = 2 / Pr_exito_caso2
print()
print("Caso L = D/2:")
print(f"  Longitud L = {L}, Separacion D = {D}")
print(f"  Probabilidad estimada P = {Pr_exito_caso2:.6f}")
print(f"  Valor teórico de 2/pi = {2/math.pi:.6f}")
print(f"  Estimacion de pi desde P = {pi_estimado:.6f}")
print(f"  pi_estimado / pi = {pi_estimado / math.pi:.6f}")
