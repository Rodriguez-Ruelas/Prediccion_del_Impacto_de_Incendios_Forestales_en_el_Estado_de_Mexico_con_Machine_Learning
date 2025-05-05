import os
import pandas as pd
import re
from datetime import datetime

folder = "data"
records = []

for fname in os.listdir(folder):
    if fname.endswith(".txt"):
        path = os.path.join(folder, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            meta = {}
            for line in lines:
                if "ESTACIÓN" in line:
                    meta['id_estacion'] = line.split(":")[1].strip()
                elif "NOMBRE" in line:
                    meta['nombre_estacion'] = line.split(":")[1].strip()
                elif "ESTADO" in line:
                    meta['estado'] = line.split(":")[1].strip()
                elif "MUNICIPIO" in line:
                    meta['municipio'] = line.split(":")[1].strip()
                elif "LATITUD" in line:
                    meta['latitud'] = line.split(":")[1].split("°")[0].strip()
                elif "LONGITUD" in line:
                    meta['longitud'] = line.split(":")[1].split("°")[0].strip()
                elif "ALTITUD" in line:
                    meta['altitud'] = line.split(":")[1].split("msnm")[0].strip()
                if "FECHA" in line:
                    break
            datos = [l for l in lines if re.match(r"\d{4}-\d{2}-\d{2}", l)]
            for l in datos:
                partes = l.strip().split()
                if len(partes) >= 5:
                    fecha = partes[0]
                    try:
                        fdt = datetime.strptime(fecha, "%Y-%m-%d")
                        if fdt.year in [2022, 2023, 2024, 2025]:
                            records.append({
                                "fecha": fdt,
                                "año": fdt.year,
                                "semana": fdt.isocalendar().week,
                                "precip_mm": partes[1] if partes[1] != "NULO" else None,
                                "evap_mm": partes[2] if partes[2] != "NULO" else None,
                                "tmax_c": partes[3] if partes[3] != "NULO" else None,
                                "tmin_c": partes[4] if partes[4] != "NULO" else None,
                                **meta
                            })
                    except:
                        continue
        except:
            continue

df = pd.DataFrame(records)
for col in ["precip_mm", "evap_mm", "tmax_c", "tmin_c", "latitud", "longitud", "altitud"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Resumen semanal
resumen = df.groupby(["id_estacion", "año", "semana"]).agg({
    "precip_mm": "mean",
    "evap_mm": "mean",
    "tmax_c": "mean",
    "tmin_c": "mean",
    "latitud": "first",
    "longitud": "first",
    "altitud": "first",
    "estado": "first",
    "municipio": "first",
    "nombre_estacion": "first"
}).reset_index()

resumen.to_excel("resumen_clima_semanal.xlsx", index=False)
print("✅ Archivo guardado como resumen_clima_semanal.xlsx")
