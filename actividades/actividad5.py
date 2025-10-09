import numpy
import json

dominio = [1, 4]

def una_integral(N):
    x = numpy.random.uniform(dominio[0], dominio[1], N)
    fdex = 1 / (x**3 + 4)
    integral_fdex_dx = numpy.mean(fdex) * (dominio[1] - dominio[0])
    return integral_fdex_dx

print(f"integral f(x)dx del {dominio[0]} al {dominio[1]} = {una_integral(1000)}")

cien_aproximaciones = [una_integral(1000) for X in range(100)]

numpy_cien_aproximaciones = numpy.array(cien_aproximaciones)
promedio = numpy_cien_aproximaciones.mean()
desv_std = numpy_cien_aproximaciones.std()
print(f"Promedio = {promedio}, desv std = {desv_std}")

aproximacion_precisa = una_integral(100000000)
error_integral_media = aproximacion_precisa - promedio
print(f"Error absoluto = {error_integral_media}")