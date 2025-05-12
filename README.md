🌲 Ciencia de Datos para Incendios Forestales: Integración y Predicción con Machine Learning
📘 Descripción
Este proyecto muestra cómo estructurar un flujo completo de ciencia de datos aplicado a problemas ambientales, como la predicción del impacto de incendios forestales. A través de la integración de datos climáticos históricos y reportes oficiales de incendios, se construye un conjunto de datos robusto que permite el entrenamiento de modelos de aprendizaje automático.

Si bien aquí se aborda el caso del Estado de México, esta metodología es ampliamente adaptable a contextos agrícolas, forestales y ecológicos en otras regiones.

⚙️ ¿Qué hace este proyecto?
Descarga y procesamiento de datos climáticos diarios (TXT) → resumen semanal.

Lectura y filtrado de reportes de incendios (Excel).

Emparejamiento espacial entre estaciones meteorológicas e incendios (por cercanía).

Unificación de datos por estación y semana.

Limpieza de valores nulos para garantizar consistencia.

Entrenamiento y validación de un clasificador multiclase (XGBoost).

Evaluación con matriz de confusión y métricas por clase.

🧪 Aplicaciones potenciales
Predicción del impacto de fenómenos ambientales (heladas, plagas, sequías)

Apoyo a decisiones de gestión de riesgo agroforestal

Modelado de relaciones clima-evento en zonas rurales

Entrenamiento de modelos con etiquetas de severidad (mínimo, moderado, severo)

Adaptación para uso en evaluaciones de impacto ambiental

🗂️ Estructura del proyecto
Script	Función
01 Descargar datos Estado.py	Descarga datos climáticos oficiales
02 Data (TXT).py	Procesa archivos TXT diarios de clima
03 Data (Excel).py	Limpia y filtra reportes de incendios
04 Union (TXT y Excel).py	Empareja por ubicación y une ambas fuentes
05 Eliminar faltantes.py	Elimina entradas con datos incompletos
06 XGBoost.py	Entrena un clasificador y genera métricas

📈 Resultados
Precisión alta en clases mayoritarias

Clasificación multiclase con XGBoost

Variables más influyentes: superficie, temperatura media, latitud y semana

Evaluación con matriz de confusión y reporte detallado

🖼️ Visual del flujo (propuesta)
¿Quieres que genere una imagen tipo diagrama con todo este flujo? Puedo hacértela enseguida para que la incluyas como flujo.png en el repositorio.



## ✍️ Cita sugerida

```
Rodríguez Ruelas, R. A. (2025). Predicción del impacto de incendios forestales mediante aprendizaje automático. GitHub Repository. https://github.com/Rodriguez-Ruelas
```
