import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Ruta dinámica del modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "lgb_credit_model.pkl")

# Configuración del panel
st.set_page_config(page_title="Simulador de Scoring Crediticio", layout="centered")

# Cargar modelo
@st.cache(allow_output_mutation=True)
def load_model(path):
    if not os.path.exists(path):
        st.error(f"Modelo no encontrado en {path}")
        st.stop()
    return joblib.load(path)

model = load_model(MODEL_PATH)

# Función para generar cliente aleatorio
def generar_cliente():
    return {
        "age": np.random.randint(21, 65),
        "income": int(max(5000, np.random.normal(40000, 12000))),
        "employment_years": np.random.randint(0, 35),
        "loan_amount": np.random.randint(1000, 20000),
        "credit_history_length": np.random.randint(1, 15),
        "num_credit_lines": np.random.randint(1, 10),
        "late_payments": np.random.poisson(1.2),
        "region": np.random.choice(["North", "South", "East", "West"]),
        "has_dependents": np.random.choice([0, 1])
    }

# Interfaz Streamlit
st.title(" Simulador de Scoring Crediticio")

modo = st.radio("Modo de ingreso de datos", ["Manual", "Simular aleatoriamente"])

if modo == "Simular aleatoriamente":
    cliente = generar_cliente()
    st.success("Cliente generado aleatoriamente:")
    st.json(cliente)
else:
    st.subheader("Ingrese los datos del cliente:")
    cliente = {
        "age": st.number_input("Edad", min_value=18, max_value=100, value=30),
        "income": st.number_input("Ingreso ($)", min_value=1000, value=30000, step=100),
        "employment_years": st.number_input("Años de empleo", min_value=0, max_value=50, value=5),
        "loan_amount": st.number_input("Monto del préstamo ($)", min_value=500, value=7000, step=100),
        "credit_history_length": st.number_input("Antigüedad crediticia (años)", min_value=1, max_value=50, value=4),
        "num_credit_lines": st.number_input("Número de líneas de crédito", min_value=1, max_value=20, value=3),
        "late_payments": st.number_input("Pagos tardíos históricos", min_value=0, max_value=100, value=1),
        "region": st.selectbox("Región", ["North", "South", "East", "West"]),
        "has_dependents": st.radio("¿Tiene dependientes?", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    }

# Cálculo de score
if st.button("Calcular Score"):
    df_input = pd.DataFrame([cliente])
    df_input["region"] = df_input["region"].astype("category")

    prob_default = model.predict_proba(df_input)[0][1]
    st.metric("Probabilidad de Default (%)", f"{prob_default*100:.2f}%")

    if prob_default >= 0.7:
        st.error(" Riesgo ALTO")
    elif prob_default >= 0.4:
        st.warning(" Riesgo MODERADO")
    else:
        st.success(" Riesgo BAJO")

# --- Autoejecución como app Streamlit ---
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
