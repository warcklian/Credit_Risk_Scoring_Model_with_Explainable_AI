# generate_credit_data.py

"""
Generate synthetic credit data for risk scoring models.

Author: Jorge Octavio Gómez González
GitHub: https://github.com/warcklian
Email: warcklian696@gmail.com
LinkedIn: https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4
"""

import pandas as pd
import numpy as np
import os

# ---------------- CONFIGURACIÓN ----------------
n_samples = 500000
output_file = "data/credit_data.csv"
# ------------------------------------------------

# Crear directorio de salida
os.makedirs("data", exist_ok=True)

# Generación reproducible
np.random.seed(42)

# Crear variables sintéticas
data = pd.DataFrame({
    "client_id": np.arange(1, n_samples + 1),
    "age": np.random.randint(21, 65, size=n_samples),
    "income": np.random.normal(40000, 12000, size=n_samples).clip(min=5000).astype(int),
    "employment_years": np.random.randint(0, 35, size=n_samples),
    "loan_amount": np.random.randint(1000, 20000, size=n_samples),
    "credit_history_length": np.random.randint(1, 15, size=n_samples),
    "num_credit_lines": np.random.randint(1, 10, size=n_samples),
    "late_payments": np.random.poisson(1.2, size=n_samples),
    "region": np.random.choice(["North", "South", "East", "West"], size=n_samples),
    "has_dependents": np.random.choice([0, 1], size=n_samples),
})

# Simular probabilidad de default
logit = (
    -0.02 * data["age"]
    - 0.00004 * data["income"]
    + 0.05 * (data["loan_amount"] / 1000)
    + 0.2 * data["late_payments"]
    + 0.1 * (data["employment_years"] < 2).astype(int)
    + 0.3 * data["has_dependents"]
)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Aplicar función logística para obtener probabilidad
default_prob = sigmoid(logit)

# Asignar default binario según esa probabilidad
data["default"] = np.random.binomial(1, default_prob)

# Guardar CSV (sobrescribiendo si existe)
data.to_csv(output_file, index=False)
print(f" Generated {n_samples} samples and saved to: {output_file}")
