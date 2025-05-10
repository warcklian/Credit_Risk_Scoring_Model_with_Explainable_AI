# train_credit_model.py

"""
Train a credit scoring model using LightGBM.

- Loads data from credit_data.csv
- Preprocesses categorical variables
- Trains LightGBM model
- Saves evaluation metrics, confusion matrix, and model

Author: Jorge Octavio Gómez González
GitHub: https://github.com/warcklian
"""

import pandas as pd
import numpy as np
import os
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# ---------------- CONFIG ----------------
DATA_PATH = "data/credit_data.csv"
MODEL_PATH = "models/lgb_credit_model.pkl"
CONF_MATRIX_PATH = "visualizations/confusion_matrix_credit.png"
REPORT_PATH = "reports/credit_score_report.csv"
# ----------------------------------------

# Verificar existencia del dataset
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"No data found at {DATA_PATH}. Run generate_credit_data.py first.")

# Cargar datos
df = pd.read_csv(DATA_PATH)

# Preprocesamiento de variables categóricas
df["region"] = df["region"].astype("category")

# Separar variables predictoras y variable objetivo
X = df.drop(columns=["client_id", "default"])
y = df["default"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Entrenar modelo LightGBM
model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Reporte de métricas
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("AUC-ROC Score:", roc_auc_score(y_test, y_proba))

# Guardar matriz de confusión como imagen
conf_mat = confusion_matrix(y_test, y_pred)
os.makedirs("visualizations", exist_ok=True)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_mat, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig(CONF_MATRIX_PATH)
plt.close()
print(f" Confusion matrix saved to {CONF_MATRIX_PATH}")

# Guardar modelo entrenado
os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f" Model saved to {MODEL_PATH}")

# Crear reporte con predicciones para dashboard
os.makedirs("reports", exist_ok=True)
df_report = X_test.copy()
df_report["default_probability"] = y_proba
df_report["predicted_default"] = y_pred
df_report["true_default"] = y_test.values
df_report.to_csv(REPORT_PATH, index=False)
print(f" Report saved to: {REPORT_PATH}")
