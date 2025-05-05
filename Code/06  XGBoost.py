import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar dataset
df = pd.read_excel("dataset_incendios_clima_limpio.xlsx")

# 2. Separar años para entrenamiento y prueba
df_train = df[df["año"] <= 2023]
df_test = df[df["año"] == 2024]

# 3. Selección de variables
features = ["tmed_c", "tmax_c", "tmin_c", "precip_mm", "evap_mm",     # Clima
            "dist_km", "altitud",                                     # Estación y ubicación
            "Superficie", "Total días / persona",                     # Datos del incendio
            "Latitud", "Longitud", "Semana.", "Año"                   # Coordenadas + tiempo
            ]

X_train = df_train[features]
X_test = df_test[features]

y_train = df_train["Clasificación primer orden"]
y_test = df_test["Clasificación primer orden"]

# 4. Codificación de etiquetas
le = LabelEncoder()
y_train_enc = le.fit_transform(y_train)
y_test_enc = le.transform(y_test)

# 5. Crear modelo XGBoost multiclase
model = xgb.XGBClassifier(
    objective="multi:softmax",
    num_class=len(le.classes_),
    eval_metric="mlogloss",
    use_label_encoder=False,
    random_state=42
)

# 6. Entrenamiento
model.fit(X_train, y_train_enc)

# 7. Predicción y evaluación
y_pred = model.predict(X_test)
print("✅ Modelo XGBoost entrenado\n")
print(classification_report(y_test_enc, y_pred, target_names=le.classes_))

# 8. Matriz de confusión
cm = confusion_matrix(y_test_enc, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="PuBuGn", xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Matriz de Confusión - XGBoost (validación 2024)")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.show()
