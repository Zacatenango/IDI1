import pandas

vt = pandas.read_excel("datosCT.xlsx", sheet_name="vt", index_col=0)

vt["Ingreso"] += 1000
vt["Utilidad"] = vt["Ingreso"] - vt["Gasto"]
promedio_gasto_utilidad_negativa = vt[ vt["Utilidad"] < 0 ]["Gasto"].mean()
ingreso_total = vt["Ingreso"].sum()
meses_utilidad_positiva = vt[ vt["Utilidad"] > 0 ].index

print(f"-------------- Sección vt --------------")
print(f"Promedio de gasto en meses de utilidad negativa: {promedio_gasto_utilidad_negativa}")
print(f"Meses de utilidad positiva: {meses_utilidad_positiva}")
print(f"\nDataframe final:\n{vt}")

cd = pandas.read_excel("datosCT.xlsx", sheet_name="8c", index_col=0)
cd = cd / 1.609
cd["gdl"] = cd["GDL"]
ciudades_mas_de_1000_millas = cd[ cd["gdl"] > 1000 ].index

print("\n-------------- Sección 8c --------------")
print(f"Serie gdl:\n{cd['gdl']}\n")
print(f"Ciudades a más de 1000 millas de Guadalajara: {ciudades_mas_de_1000_millas}\n")
print(f"Dataframe final:\n{cd}")

