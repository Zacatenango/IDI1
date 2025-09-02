import pandas

_dataframe = pandas.read_excel("datosPE.xlsx")
print(_dataframe)

# Crear una columna nueva sale sumando columnas
_dataframe["Suma"] = _dataframe["Valor"] + _dataframe["Real"]

# La sumatoria de una columna entera sale con sum()
sumatoria = _dataframe["Suma"].sum()

# Si uso una comparación lógica, PANDAS tira una columna que tiene True donde se cumple la condición
o_posiciones = _dataframe["Vocal"] == "o"

# Si indexo mi dataframe con una columna con True o False, me filtra el DF
dataframe_o = _dataframe[o_posiciones]

# Notación corta
suma_real_E = _dataframe[ _dataframe["Vocal"] == "e" ]["Real"].sum()
