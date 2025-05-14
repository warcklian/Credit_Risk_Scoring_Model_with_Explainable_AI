# 💳 Credit Risk Scoring Model with Explainable AI

**Autor:** Jorge Octavio Gómez González  
📫 [Email](mailto:warcklian696@gmail.com) | 🔗 [LinkedIn](https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4) | 💻 [GitHub](https://github.com/warcklian)

---

## 📌 Descripción

Este proyecto demuestra una solución completa de *Credit Risk Scoring* utilizando **modelos de machine learning**, datos sintéticos generados desde cero y visualizaciones interactivas con **Streamlit**. Ideal como base para sistemas de scoring crediticio en producción o pruebas de concepto para fintechs.

---

## 🚀 Aplicaciones Interactivas

🔍 **Dashboard de Riesgo Crediticio**  
Análisis de modelo, métricas de rendimiento y visualizaciones dinámicas.  
🔗 [Probar](https://creditriskscoringmodelwithexplainableai-jqpautq6kdi4dsvjv6hn6c.streamlit.app/)

🧮 **Simulador de Score para Nuevos Clientes**  
Simula clientes aleatorios o ingresa uno manualmente para estimar su score.  
🔗 [Probar](https://creditriskscoringmodelwithexplainableai-qnptijqfh3gmyveztgdkhq.streamlit.app/)

---

## 🧠 Características Principales

- 📊 Generación de datos sintéticos financieros.
- ⚙️ Entrenamiento de modelos con LightGBM.
- 🧪 Evaluación del modelo: AUC, precisión, recall y matriz de confusión.
- 📉 Visualización interactiva con Streamlit y Seaborn.
- 🧮 Simulación de scoring en tiempo real desde frontend web.
- 📦 Proyecto organizado, modular y listo para producción o ampliación.

---

## 🗂️ Estructura del Proyecto

```plaintext
Credit_Risk_Scoring_Model_with_Explainable_AI/
├── data/                # Datos generados (.csv)
├── models/              # Modelos entrenados (.pkl)
├── reports/             # Resultados con predicciones
├── visualizations/      # Matriz de confusión
├── generate_credit_data.py     # Generación de datos sintéticos
├── train_credit_model.py       # Entrenamiento y evaluación
├── score_client.py             # Dashboard Streamlit
├── simulate_score.py           # Simulador interactivo
├── requirements.txt            # Dependencias
└── README.md                   # Documentación
⚙️ Instalación y Uso
1. Clonar repositorio y crear entorno:

git clone https://github.com/warcklian/Credit_Risk_Scoring_Model_with_Explainable_AI.git
cd Credit_Risk_Scoring_Model_with_Explainable_AI
python -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
2. Ejecutar el pipeline completo:

python generate_credit_data.py       # Paso 1: Generar datos
python train_credit_model.py         # Paso 2: Entrenar modelo
streamlit run score_client.py        # Paso 3: Dashboard
streamlit run simulate_score.py      # (opcional) Simulador
📊 Métricas Clave del Modelo
Métrica	Descripción	Valor Esperado
AUC-ROC	Discriminación entre clientes buenos y de alto riesgo	> 0.70
Accuracy	Precisión global del modelo	> 0.75
Precision (1)	Qué tan confiables son las predicciones de default	Alto
Recall (1)	Capacidad del modelo para capturar clientes realmente riesgosos	> 0.50
Confusión Matrix	Visual de errores y aciertos en clasificación	-

📦 Requisitos

Python >= 3.9

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
lightgbm
joblib
Instalar con:

pip install -r requirements.txt
📝 Licencia
Este proyecto está licenciado bajo MIT.

🤝 Contribuciones
¡Pull requests y sugerencias son bienvenidas! Siéntete libre de clonar, modificar y compartir.

📅 Última actualización: mayo 2025

---

### ¿Qué incluye esta versión?

- ✅ Tono profesional + lenguaje técnico para portafolio.
- ✅ Enlaces públicos a las apps funcionando.
- ✅ Estructura Markdown clara para GitHub.
- ✅ Métricas del modelo en tabla.
- ✅ Lista de librerías y comandos reproducibles.

---

¿Te gustaría que lo convierta también a PDF o te ayude a incluirlo en tu release como documentación lista para descargar?