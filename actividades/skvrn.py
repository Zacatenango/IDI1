import numpy

# Generalmente, en las listas de datos de Python son de tipos de datos surtidos...
numeritos = [1,2,3,4]
surtido = [1, 2.9, True, "Acoyani", numpy]

# Pero en Numpy, los arrays son de un solo tipo de datos
arr_numeritos = numpy.array(numeritos)
print(f"Numeritos: {arr_numeritos}")

# Si a numpy.array() le paso una lista surtida, el tipo de datos dependerá de qué tipos de datos
# haya. Numpy tiene una jerarquía para eso.
arr_surtido = numpy.array(surtido)
print(f"Surtido: {arr_surtido}")

# A diferencia de Python, que maneja precisión arbitraria, en Numpy los números son con los tipos
# de datos de C.
numerote = 10000000000000000000000000000000000000000000000000000000000000000000
arr_numerote = numpy.array(numerote)
print(f"Numerote: {arr_numerote}")

# Si necesito un tipo de datos determinado, para eso sirve el parámetro dtype
entero64 = 238932893289
arr_entero64 = numpy.array(entero64, dtype="int64")
print(f"Entero de 64 bits: {arr_entero64}")

# Si necesito un array secuencial, puedo ya sea usar un inline for estándar, o la función arange
secuencia_vanilla = [X for X in range(100)]
arr_secuencia_vanilla = numpy.array(secuencia_vanilla)
arr_secuencia_numpy = numpy.arange(100)

# Igual que en MATLAB, operar un vector con un escalar aplica la operación a cada elemento del vector
arr_secuencia_cuadrados = arr_secuencia_numpy ** 2

# Igual que en MATLAB, puedo convertir un vector en una matrix con reshape()
# C significa "estilo C" (indexado primero por filas), F significa "estilo FORTRAN" (indexado 
# primero por columnas)
M10x10_secuencia = numpy.reshape(arr_secuencia_numpy, (10,10), "C")

# Para sacar la suma de una matriz de Numpy, es necesario usar la función de Numpy.
# Esto, ya que en Python vanilla no existen las matrices estrictamente hablando; lo que existiría
# sería una lista de listas.
M10x10_suma = M10x10_secuencia.sum()

# Si quiero sacar la suma por fila, especifico cuál axis quiero usar
M10x10_suma_filas = M10x10_secuencia.sum(0)
print(f"Suma por fila: {M10x10_suma_filas}")

# Para rebanar mi matriz, uso notación de MATLAB
# En notación de rango matemático, el rango que obtengo es [inicio, final)
filas3_5 = M10x10_secuencia[3:6]
print(f"Filas 3-5: {filas3_5}")

# Para contar los elementos que cumplen alguna condición, primero aplico un condicional a mi matriz
# Eso me da como resultado una matriz booleana
M10x10_secuencia_multiplosde10 = M10x10_secuencia % 10 == 0
# Luego saco la sumatoria de la matriz booleana; hacer eso me dice cuántos son True
multiplosde10 = M10x10_secuencia_multiplosde10.sum()
print(f"Hay {multiplosde10} múltiplos de 10 en la matriz")
