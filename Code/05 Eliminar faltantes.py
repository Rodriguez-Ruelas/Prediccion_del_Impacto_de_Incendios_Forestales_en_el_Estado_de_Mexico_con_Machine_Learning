import pandas as pd

# Cargar el dataset combinado
df = pd.read_excel("dataset_incendios_clima.xlsx")

# Eliminar todas las filas que tengan al menos un valor faltante
df_limpio = df.dropna()

# Guardar el dataset limpio
df_limpio.to_excel("dataset_incendios_clima_limpio.xlsx", index=False)

print(f"✅ Dataset limpio guardado como 'dataset_incendios_clima_limpio.xlsx'")
print(f"🔍 Filas originales: {len(df)}, Filas después de limpiar: {len(df_limpio)}")
