import os
import pandas as pd

carpeta = "data"
registros = []

for archivo in os.listdir(carpeta):
    if archivo.endswith(".xlsx"):
        try:
            xls = pd.ExcelFile(os.path.join(carpeta, archivo))
            for hoja in xls.sheet_names:
                try:
                    df = pd.read_excel(xls, sheet_name=hoja, header=1)
                    if 'Estado' in df.columns:
                        filtro = df['Estado'].astype(str).str.lower().str.contains("méxico")
                        registros.append(df[filtro])
                except:
                    continue
        except:
            continue

df_final = pd.concat(registros, ignore_index=True)
df_final.to_excel("incendios_estado_mexico.xlsx", index=False)
print("✅ Archivo guardado como incendios_estado_mexico.xlsx")
