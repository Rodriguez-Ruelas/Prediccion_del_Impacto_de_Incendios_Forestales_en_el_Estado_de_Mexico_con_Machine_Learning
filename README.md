# 🔥 Ciencia de Datos para el Análisis de Incendios Forestales en el Estado de México

## 📘 Descripción general

Este proyecto presenta un enfoque práctico de ciencia de datos para analizar el impacto de incendios forestales en el Estado de México, combinando procesamiento estadístico, limpieza de datos y algoritmos de aprendizaje automático. El objetivo es demostrar cómo una **metodología estructurada puede aprovechar datos públicos** para resolver problemas ambientales complejos, como la predicción de la severidad de incendios forestales.

La lógica desarrollada es completamente replicable y puede adaptarse a contextos agrícolas, ecológicos, forestales o urbanos que demanden integración de datos climáticos, espaciales y operativos para tomar decisiones informadas.

## 🎯 Propósito

- Integrar fuentes de datos diversos (climáticos, operativos y geográficos)
- Aplicar limpieza y preprocesamiento estadístico de datos
- Entrenar modelos predictivos (XGBoost) que clasifiquen la severidad del impacto
- Evaluar la importancia de variables y balancear clases mediante técnicas como SMOTE

## 🧪 ¿Por qué es relevante?

Este flujo de trabajo puede ser utilizado en múltiples áreas:

- Predicción de rendimiento agrícola en parcelas con distintas condiciones climáticas
- Evaluación de riesgo de plagas o enfermedades forestales
- Clasificación de zonas prioritarias para intervención ambiental
- Predicción de eventos extremos relacionados con el clima

## 🔄 Flujo de trabajo

<p align="center">
  <img src="https://github.com/Rodriguez-Ruelas/Prediccion_del_Impacto_de_Incendios_Forestales_en_el_Estado_de_Mexico_con_Machine_Learning/blob/main/Image/diagrama.png" width="650" alt="Flujo del proyecto"/>
  <br/>
  <sub><b>Figura:</b> Diagrama del flujo de trabajo implementado para el análisis y modelado de datos de incendios forestales.</sub>
</p>

## 🧩 Estructura del repositorio

El proyecto se compone de seis scripts secuenciales:

| Script                            | Descripción                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `01 Descargar datos Estado.py`    | Descarga y filtra incendios del Estado de México desde archivos oficiales  |
| `02 Data (TXT).py`                | Procesamiento de archivos .txt climáticos diarios                          |
| `03 Data (Excel).py`              | Procesamiento de datos semanales climáticos en Excel                       |
| `04 Union (TXT y Excel).py`       | Integración de ambas fuentes climáticas, más datos de incendios            |
| `05 Eliminar faltantes.py`        | Eliminación de registros con datos incompletos                             |
| `06 XGBoost.py`                   | Modelado predictivo con XGBoost, balanceo de clases con SMOTE y evaluación |

## 🛠️ Tecnologías empleadas

- Python 3.11+
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `xgboost`, `scikit-learn`
- `imbalanced-learn` para SMOTE

## 📃 Dataset

- Incendios forestales en el Estado de México (2022–2025)
- Datos climáticos diarios y semanales
- Variables utilizadas: temperatura media/máx/mín, precipitación, evaporación, altitud, superficie, distancia a municipios, días/hombre, entre otras

## 📈 Resultados clave

- Precisión general superior al 90% en clases frecuentes
- La clase “severo” es difícil de predecir por desbalance
- Variables más importantes: superficie quemada, altitud, semana del año, distancia
- El modelo XGBoost se comportó robustamente con variables numéricas

---

## 👤 Autor

**Raúl Alfonso Rodríguez Ruelas**  
[GitHub](https://github.com/Rodriguez-Ruelas)  
[LinkedIn](https://www.linkedin.com/in/raul-rodriguez-ruelas-20634a171/)

---

> *Rodríguez Ruelas, R. A. (2025). Ciencia de Datos para el Análisis de Incendios Forestales. GitHub Repository. https://github.com/Rodriguez-Ruelas*
