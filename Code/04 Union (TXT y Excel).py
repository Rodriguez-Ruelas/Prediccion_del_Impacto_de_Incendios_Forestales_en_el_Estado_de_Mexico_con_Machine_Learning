import pandas as pd
import numpy as np
from scipy.spatial import cKDTree

# Cargar datos ya limpios y preparados
df_clima = pd.read_excel("resumen_clima_semanal.xlsx")  # Debe tener: id_estacion, año, semana, latitud, longitud
df_incendios = pd.read_excel("incendios_estado_mexico.xlsx")  # Debe tener: Latitud, Longitud, Semana., Año

# 1️⃣ Limpiar datos nulos en coordenadas
df_clima = df_clima.dropna(subset=["latitud", "longitud"])
df_incendios = df_incendios.dropna(subset=["Latitud", "Longitud"])

# 2️⃣ Convertir tipos de semana y año
df_incendios["semana"] = pd.to_numeric(df_incendios["Semana."], errors="coerce")
df_incendios["año"] = pd.to_numeric(df_incendios["Año"], errors="coerce")

# 3️⃣ Buscar estación climática más cercana con KDTree
tree = cKDTree(df_clima[["latitud", "longitud"]].values)
distancias, indices = tree.query(df_incendios[["Latitud", "Longitud"]].values)

# 4️⃣ Asignar la estación más cercana a cada incendio
df_incendios["id_estacion"] = df_clima.iloc[indices]["id_estacion"].values
df_incendios["dist_km"] = distancias * 111  # Convertimos de grados a km

# 5️⃣ Hacer unión exacta por estación + semana + año
df_unido = pd.merge(
    df_incendios,
    df_clima,
    how="left",
    on=["id_estacion", "año", "semana"],
    suffixes=("_incendio", "_clima")
)

# 6️⃣ Guardar archivo final
df_unido.to_excel("dataset_incendios_clima.xlsx", index=False)
print("✅ ¡Archivo generado exitosamente como 'dataset_incendios_clima.xlsx'!")
