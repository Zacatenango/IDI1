"""
Simulación Montecarlo del problema de la Aguja de Buffon.

Calcula la probabilidad de que una aguja de longitud L caiga cruzando líneas separadas por distancia D.
Usa N experimentos. Muestra resultados para L = D y L = D/2.

También estima pi usando la relación P = 2 / pi cuando L = D (aproximación).
"""

import random
import math


def buffon_trial(L, D):
   """Realiza un único experimento de la aguja de Buffon.

   - x: distancia del centro de la aguja a la línea más cercana (en [0, D/2])
   - theta: ángulo respecto a las líneas (en [0, pi/2])

   Devuelve True si la aguja cruza una línea.
   """
   # posición del centro desde la línea más cercana (simetría -> [0, D/2])
   x = random.uniform(0, D / 2)
   # ángulo entre 0 y pi/2 (simetría por reflexión)
   theta = random.uniform(0, math.pi / 2)
   # distancia desde el centro hasta el extremo proyectada perpendicular a las líneas
   half_proj = (L / 2.0) * math.sin(theta)
   return half_proj >= x


def estimate_probability(L, D, N):
   hits = 0
   for _ in range(N):
      if buffon_trial(L, D):
         hits += 1
   return hits / N


def estimate_pi_from_prob(P):
   """Estima pi usando la relación P = 2 / pi válida cuando L = D.

   Devuelve la estimación pi_hat = 2 / P.
   """
   if P <= 0:
      return float('inf')
   return 2.0 / P


def main():
   N = 100000
   D = 1.0

   # Caso 1: L = D
   L1 = D
   p1 = estimate_probability(L1, D, N)
   pi_est = estimate_pi_from_prob(p1)

   # Caso 2: L = D/2
   L2 = D / 2.0
   p2 = estimate_probability(L2, D, N)

   print(f"Experimentos N = {N}")
   print("Caso L = D:")
   print(f"  Longitud L = {L1}, Separacion D = {D}")
   print(f"  Probabilidad estimada P = {p1:.6f}")
   print(f"  Valor teórico 2/pi = {2/math.pi:.6f}")
   print(f"  Estimacion de pi desde P: pi_hat = {pi_est:.6f}")
   print()
   print("Caso L = D/2:")
   print(f"  Longitud L = {L2}, Separacion D = {D}")
   print(f"  Probabilidad estimada P = {p2:.6f}")
   # Comentario sobre estimación de pi
   print()
   print("Conclusión:")
   print("  - Cuando L = D la probabilidad teórica es 2/pi. Usando Montecarlo podemos estimar P y despejar pi (pi_hat = 2/P).")
   print("  - Cuando L = D/2 la probabilidad cambia (no es 2/pi).")
   print("  - Sí, es posible estimar pi con este juego cuando L = D; la precisión depende de N (error ~ 1/sqrt(N)).")


if __name__ == '__main__':
   main()

