import pandas as pd
import numpy as np
from scipy.spatial import cKDTree

# Cargar datos
df_clima = pd.read_excel("resumen_clima_semanal.xlsx")
df_incendios = pd.read_excel("incendios_estado_mexico.xlsx")

# 1️⃣ Limpiar nulos en coordenadas
df_clima = df_clima.dropna(subset=["latitud", "longitud"])
df_incendios = df_incendios.dropna(subset=["Latitud", "Longitud"])

# 2️⃣ Convertir tipos
df_incendios["semana"] = pd.to_numeric(df_incendios["Semana."], errors="coerce")
df_incendios["año"] = pd.to_numeric(df_incendios["Año"], errors="coerce")

# 3️⃣ Estación más cercana
tree = cKDTree(df_clima[["latitud", "longitud"]].values)
distancias, indices = tree.query(df_incendios[["Latitud", "Longitud"]].values)

df_incendios["id_estacion"] = df_clima.iloc[indices]["id_estacion"].values
df_incendios["dist_km"] = distancias * 111  # grados → km

# 4️⃣ Unir con clima
df_unido = pd.merge(
    df_incendios,
    df_clima,
    how="left",
    on=["id_estacion", "año", "semana"],
    suffixes=("_incendio", "_clima")
)

# 5️⃣ Agregar tmed_c como promedio de tmax_c y tmin_c
df_unido["tmed_c"] = (df_unido["tmax_c"] + df_unido["tmin_c"]) / 2

# 6️⃣ Guardar
df_unido.to_excel("dataset_incendios_clima.xlsx", index=False)
print("✅ ¡Archivo generado exitosamente como 'dataset_incendios_clima.xlsx'!")
