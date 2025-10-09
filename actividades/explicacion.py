import numpy

N = 1000000
pxp = numpy.random.uniform(0, 1, (N, 2))
dentro = numpy.sum(pxp**2, 1) <= 1
estimacion_pi = 4 * sum(dentro) / N
print(f"pi = {estimacion_pi}")

N = 100000
gano = 0
for X in range(N):
    tiro = sum(numpy.random.choice(range(1, 7), 2))
    if tiro in [7, 11]:
        gano += 1
    elif not tiro in [2,3,12]:
        tiro2 = -1
        while (tiro2 not in [7, tiro]):
            tiro2 = sum(numpy.random.choice(range(1, 7), 2))
            if tiro2 == tiro:
                gano += 1

Pr_ganar = gano / N
print(f"Pr(ganar en el CRAPS) = {Pr_ganar}")

# Sacar una integral numérica con método de Montecarlo
N = 1000000000
dominio = [0, 1]
x = numpy.random.uniform(dominio[0], dominio[1], N)
f_de_x = x**2
integral_fdex_dx = numpy.mean(f_de_x) * (dominio[1] - dominio[0])
print(f"integral f(x)dx del 0 al 1 = {integral_fdex_dx}")

dominio = [2, 3]
x = numpy.random.uniform(dominio[0], dominio[1], N)
f_de_x = 1 / (x**3 - (2 * x))
integral_fdex_dx = numpy.mean(f_de_x) * (dominio[1] - dominio[0])
print(f"integral f(x)dx del 0 al 1 = {integral_fdex_dx}")

