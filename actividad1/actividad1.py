import pandas

# Extraer datos del archivo adjunto
pesos = pandas.read_excel("datosPE.xlsx", index_col="ID Persona")

# Sacar el vector de IMC
pesos["IMC"] = pesos["Peso"] / (pesos["Estatura"] ** 2)

# Sacar el promedio de pesos y estaturas
print(f"Promedio de pesos: {pesos['Peso'].mean()}")
print(f"Promedio de estaturas: {pesos['Estatura'].mean()}")

# Sacar el ID del más gordo y del más chaparro
print(f"La persona #{pesos['Peso'].idxmax()} es la de mayor peso")
print(f"La persona #{pesos['Estatura'].idxmin()} es la de menor estatura")

# Sacar el vector de las estaturas cuyo IMC es mayor que 28
estaturas_IMC_28 = pesos[ pesos["IMC"] > 28 ]["Estatura"]

# Imprimo el resultado
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
print("Vector de IMC:")
print(pesos["IMC"])
print("\nEstaturas cuyo IMC es mayor que 28")
print(estaturas_IMC_28)
