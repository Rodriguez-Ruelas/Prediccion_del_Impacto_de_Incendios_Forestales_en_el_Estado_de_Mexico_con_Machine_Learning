# 🔥 Predicción del Impacto de Incendios Forestales en el Estado de México con Machine Learning

## 📅 Periodo de estudio

2022 - 2025

## 📚 Resumen

Los incendios forestales constituyen una amenaza creciente para los ecosistemas y la población del Estado de México. Este proyecto presenta un enfoque basado en aprendizaje automático para predecir el **impacto** (clasificado en mínimo, moderado o severo) y la **superficie afectada** por incendios forestales, integrando datos climáticos semanales, geográficos y operativos.

Se construyó una base de datos a partir de reportes oficiales de incendios (2022–2025) y registros climáticos diarios, que fueron procesados y unificados mediante:

* Limpieza de datos
* Georreferenciación y emparejamiento espacial (por distancia)
* Agregación semanal de variables climáticas

Posteriormente, se entrenaron modelos de clasificación (XGBoost) y regresión (Red neuronal artificial - ANN). Los resultados muestran una alta precisión general para predecir impactos mínimos, pero también evidencian desafíos ante la desproporción de clases. En cuanto a la regresión, el modelo ANN mostró un desempeño bajo con R² negativo.

Este trabajo sienta las bases para una herramienta predictiva útil en la gestión y prevención de incendios forestales.

## 🔍 Tecnologías y herramientas

* Python 3.13
* pandas, numpy, matplotlib, seaborn
* scikit-learn
* xgboost
* SMOTE (imbalanced-learn)

## 💡 Objetivos

* Predecir la severidad del impacto de incendios usando clasificadores (XGBoost)
* Estimar la superficie quemada con una red neuronal de regresión (ANN)
* Analizar la influencia de variables climáticas y espaciales en la severidad

## 📊 Scripts

```
/ANN/
├── 01 Descargar datos  Estado.py
├── 02 Data (TXT).py
├── 03 Data (Excel).py
├── 04 Union (TXT y Excel).py
├── 05 Eliminar faltantes.py
├── 06  XGBoost.py
├── 07 ANN.py

```

## 📃 Dataset

* Incendios forestales (datos oficiales 2022–2025)
* Datos climáticos diarios (convertidos a semanales)
* Variables: temperatura media/máxima/mínima, precipitación, evaporación, altitud, distancia, superficie quemada, entre otras

## 📊 Resultados principales

* ✅ **Precisión > 90%** en clases mayoritarias usando XGBoost
* ❗ Dificultades al clasificar clases raras (severo, moderado)
* 🌿 Superficie, latitud, semana y días/persona = variables más relevantes
* 🔵 **Regresión ANN (Superficie)**: MAE = 23.82 | RMSE = 70.67 | R² = -0.40 (desempeño bajo)

## 🌐 Autor

Raúl Alfonso Rodríguez Ruelas
[GitHub](https://github.com/Rodriguez-Ruelas)
[LinkedIn](https://www.linkedin.com/in/raul-rodriguez-ruelas-20634a171)

## ✍️ Cita sugerida

```
Rodríguez Ruelas, R. A. (2025). Predicción del impacto de incendios forestales mediante aprendizaje automático. GitHub Repository. https://github.com/Rodriguez-Ruelas
```
