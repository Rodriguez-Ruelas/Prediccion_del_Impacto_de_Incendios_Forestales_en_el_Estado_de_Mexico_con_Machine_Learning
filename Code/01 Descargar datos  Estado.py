import os
import requests
from tqdm import tqdm

# Crear carpeta si no existe
output_folder = "descargas_estado_mexico"
os.makedirs(output_folder, exist_ok=True)

# Rango de claves que encontraste en la tabla
claves_estaciones = range(15001, 15399)  # puedes ajustar según la tabla

# URL base
base_url = "https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios/mex/dia{:05d}.txt"

# Descargar archivos
for clave in tqdm(claves_estaciones):
    url = base_url.format(clave)
    filename = f"dia{clave:05d}.txt"
    filepath = os.path.join(output_folder, filename)
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and len(response.text.strip()) > 10:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response.text)
        else:
            print(f"⚠️ Archivo {filename} no disponible.")
    except Exception as e:
        print(f"❌ Error con {filename}: {e}")

print("✅ Descarga completa.")
