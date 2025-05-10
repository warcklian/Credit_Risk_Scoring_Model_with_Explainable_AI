# dashboard_credit.py

"""
Dashboard interactivo para revisión de scores de crédito.

- Carga de resultados desde CSV
- Filtros dinámicos por predicción de default
- Gráficos embebidos: score vs ingreso, edad, etc.

Autor: Jorge Octavio Gómez González
Fecha: 2025-05-10
"""

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración del panel
st.set_page_config(page_title="Dashboard Crediticio", layout="wide")
DATA_PATH = "reports/credit_score_report.csv"

# Cargar datos con caché
@st.cache
def load_data(path):
    return pd.read_csv(path)

# Validar existencia del archivo
if not os.path.exists(DATA_PATH):
    st.error(f"No se encontró el archivo de resultados: {DATA_PATH}")
    st.stop()

df = load_data(DATA_PATH)

# Sidebar con filtros
st.sidebar.header("Filtros")
default_filtrado = st.sidebar.selectbox("Mostrar registros:", ["Todos", "Solo DEFAULT", "Solo NO DEFAULT"])
umbral = st.sidebar.slider("Umbral de Probabilidad de Default (%)", 0, 100, 50)

# Filtrado de datos
df_filtrado = df.copy()
if default_filtrado == "Solo DEFAULT":
    df_filtrado = df_filtrado[df_filtrado["predicted_default"] == 1]
elif default_filtrado == "Solo NO DEFAULT":
    df_filtrado = df_filtrado[df_filtrado["predicted_default"] == 0]

df_filtrado = df_filtrado[df_filtrado["default_probability"] * 100 >= umbral]

# Título y resumen
st.title("Score de Riesgo Crediticio")
st.markdown("Este dashboard permite analizar las predicciones de riesgo crediticio con base en datos simulados.")

st.metric("Total de Registros", len(df))
st.metric("Registros Filtrados", len(df_filtrado))

# Tabla filtrada
st.subheader("Clientes Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Visualizaciones
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de Scores")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["default_probability"], bins=20, kde=True, ax=ax1)
    ax1.set_title("Histograma de Probabilidad de Default")
    st.pyplot(fig1)

with col2:
    st.subheader("Ingreso vs Riesgo de Default")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="income", y="default_probability", hue="predicted_default", palette="coolwarm", ax=ax2)
    ax2.set_title("Relación Ingreso - Riesgo")
    st.pyplot(fig2)

# Métricas del modelo
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

st.subheader("Métricas de Evaluación del Modelo")

if {"true_default", "predicted_default", "default_probability"}.issubset(df.columns):
    y_true = df["true_default"]
    y_pred = df["predicted_default"]
    y_proba = df["default_probability"]

    auc = roc_auc_score(y_true, y_proba)
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)

    col3, col4 = st.columns(2)
    with col3:
        st.metric("AUC-ROC", f"{auc:.3f}")
        st.metric("Accuracy", f"{report['accuracy']:.3f}")
    with col4:
        st.metric("Precision (Default)", f"{report['1']['precision']:.3f}")
        st.metric("Recall (Default)", f"{report['1']['recall']:.3f}")

    fig3, ax3 = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax3)
    ax3.set_xlabel("Predicción")
    ax3.set_ylabel("Valor Real")
    ax3.set_title("Matriz de Confusión")
    st.pyplot(fig3)

    st.markdown("""
**Descripción de las Métricas**

- **AUC-ROC (Área Bajo la Curva ROC)**:  
  Mide la capacidad del modelo para distinguir entre clases (default y no default).  
  - Rango: 0.5 (azar) a 1.0 (perfecto).  
  - Valor esperado: > 0.70 para modelos aceptables.

- **Accuracy (Precisión Global)**:  
  Porcentaje total de predicciones correctas.  
  - Puede ser engañosa si las clases están desbalanceadas.  
  - Valor razonable: > 0.75.

- **Precision (Default)**:  
  De todos los clientes que el modelo predijo como *default*, ¿cuántos realmente lo son?  
  - Alta precisión evita falsos positivos.  
  - Ideal para minimizar el rechazo de clientes buenos.

- **Recall (Default)**:  
  De todos los clientes que realmente hacen *default*, ¿cuántos detectó el modelo?  
  - Alta sensibilidad evita pasar por alto casos de riesgo real.  
  - Valor esperado: > 0.5 si el modelo está bien calibrado.

- **Matriz de Confusión**:  
  Muestra la cantidad de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.  
  - Ayuda a entender los errores específicos del modelo.
""")
else:
    st.warning("Las columnas 'true_default', 'predicted_default', 'default_probability' son necesarias para calcular métricas.")

# Autoabrir navegador
if __name__ == "__main__":
    import threading
    import time
    import webbrowser
    import streamlit.web.bootstrap

    if os.environ.get("STREAMLIT_SERVER_RUN_ONCE", "0") != "1":
        def abrir_navegador():
            time.sleep(1.5)
            webbrowser.open("http://localhost:8501")

        os.environ["STREAMLIT_SERVER_RUN_ONCE"] = "1"
        threading.Thread(target=abrir_navegador).start()
        streamlit.web.bootstrap.run(__file__, "", [], {})
