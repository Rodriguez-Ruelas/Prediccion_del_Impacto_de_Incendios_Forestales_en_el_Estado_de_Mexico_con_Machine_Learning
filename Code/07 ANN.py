import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar datos
df = pd.read_excel("dataset_incendios_clima_limpio.xlsx")

# 2. Variables predictoras (X) y objetivo (y)
X = df[[
    "tmed_c", "tmax_c", "tmin_c", "precip_mm", "evap_mm",
    "dist_km", "altitud", "Total días / persona",
    "Latitud", "Longitud", "Semana.", "Año"
]]
y = df["Superficie"]

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Modelo ANN
model = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=2000, random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Predicción
y_pred = model.predict(X_test_scaled)

# 7. Evaluación
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("✅ Modelo de regresión entrenado con éxito.")
print(f"📊 MAE: {mae:.2f} | RMSE: {rmse:.2f} | R²: {r2:.2f}")

# 8. Visualización
plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Superficie real (ha)")
plt.ylabel("Superficie predicha (ha)")
plt.title("🔵 ANN - Superficie predicha vs. real")
plt.grid(True)
plt.tight_layout()
plt.show()
