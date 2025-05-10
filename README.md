
# Credit Risk Scoring Model with Explainable AI

**Author**: Jorge Octavio Gómez González  
**Email**: warcklian696@gmail.com  
**GitHub**: [warcklian](https://github.com/warcklian)  
**LinkedIn**: [Jorge Octavio Gómez González](https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4)

---

## 📌 Description

This project simulates a complete pipeline for credit scoring using synthetic financial data. It includes data generation, model training using LightGBM, prediction reporting, and an interactive Streamlit dashboard for reviewing scoring results and evaluation metrics.

---

## 🧠 Features

- Synthetic client credit data generation
- Model training using LightGBM
- Dashboard with default risk visualizations
- Evaluation metrics: AUC-ROC, accuracy, precision, recall
- Real-time filtering by probability and prediction
- Explainable metrics and visual feedback

---

## 🗂️ Project Structure

Credit_Risk_Scoring_Model_with_Explainable_AI/
│
├── data/ # Generated input data (CSV)
├── reports/ # Model predictions and metrics (CSV)
├── models/ # Trained ML model (LightGBM)
├── visualizations/ # Confusion matrix plot
├── generate_credit_data.py # Synthetic data generator
├── train_credit_model.py # Train and evaluate the model
├── score_client.py # Streamlit dashboard
├── README.md # Project documentation
└── requirements.txt # Python dependencies

---

## ⚙️ Requirements

Tested on:

```text
Python 3.10

Dependencies:
- pandas==2.2.3
- numpy==1.26.4
- lightgbm==4.3.0
- scikit-learn==1.3.2
- matplotlib==3.8.4
- seaborn==0.13.2
- joblib==1.4.2
- streamlit==1.16.0
Install all dependencies:

pip install -r requirements.txt
(Optional) Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
🚀 Usage
Generate synthetic data:

python generate_credit_data.py
Train the model:

python train_credit_model.py
Launch the dashboard:

streamlit run score_client.py
The dashboard will open at http://localhost:8501.

📊 Model Metrics Description (Shown in Dashboard)
AUC-ROC: Measures model's ability to distinguish between default and non-default.

Expected range: 0.5 (random) to 1.0 (perfect)

Good value: > 0.70

Accuracy: Percentage of all correctly predicted samples.

May be misleading in imbalanced datasets.

Acceptable: > 0.75

Precision (Default): Correct predictions among those classified as default.

Helps avoid false positives.

Goal: High for risk-sensitive institutions.

Recall (Default): Proportion of actual defaults correctly predicted.

Important for capturing risky clients.

Target: > 0.5

Confusion Matrix: Breakdown of prediction outcomes (TP, FP, TN, FN).

📝 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests and suggestions are welcome. Please fork the repo and submit your changes!

Last updated: 2025-05-10