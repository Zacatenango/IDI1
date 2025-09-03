import numpy

L = [X for X in range(50) if (X % 2) == 0]
A = numpy.array(L)
print(f"Séptimo item de A: {A[7]}; Posiciones 3-9: {A[3:10]}; Últimos 3 en orden descendente: {A[-1:-3]}")
B = numpy.array(range(20, 5, 3))
C = B[::-1]
D = numpy.linspace(2, 30, 100)
print(f"Tamaño de paso para generar D: {D[1] - D[0]}")
E = numpy.linspace(5, 100, dtype="int")
I = A[ (A % 3 == 0) ]
F = numpy.reshape(D, (10,10), "C")
G = numpy.reshape(D, (10,10), "F")
M = G[0:2, 2:6]
N = (G**2) - 3
print("SI" if numpy.any(N % 17 == 0) else "NO")
print(f"{F[2]}, {G[:,3]}")
H = F + G
H[H<30] = 0; K = H
