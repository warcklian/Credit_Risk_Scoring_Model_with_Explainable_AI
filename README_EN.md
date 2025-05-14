# 💳 Credit Risk Scoring Model with Explainable AI

**Author:** Jorge Octavio Gómez González  
📫 [Email](mailto:warcklian696@gmail.com) | 🔗 [LinkedIn](https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4) | 💻 [GitHub](https://github.com/warcklian)

---

## 📌 Project Overview

This repository presents a complete and modular **credit scoring system** built with Python and Streamlit. It simulates realistic client profiles, trains a LightGBM model, and offers two interactive web applications: one for dashboard visualization and one for real-time scoring simulation.

Perfect for portfolio use, fintech prototype evaluations, or machine learning demonstrations in finance.

---

## 🚀 Interactive Applications

🔍 **Credit Risk Dashboard**  
Explore model performance, confusion matrix, and prediction distribution.  
🔗 [Launch Dashboard](https://creditriskscoringmodelwithexplainableai-jqpautq6kdi4dsvjv6hn6c.streamlit.app/)

🧮 **Client Score Simulator**  
Enter client data manually or generate random clients to evaluate risk score.  
🔗 [Try Simulator](https://creditriskscoringmodelwithexplainableai-qnptijqfh3gmyveztgdkhq.streamlit.app/)

---

## 🧠 Key Features

- 📊 Synthetic financial data generator with logic-based default probabilities.
- ⚙️ Machine learning model training using LightGBM.
- 📉 Model evaluation using AUC-ROC, accuracy, precision, and recall.
- 🖥️ Interactive dashboards and score simulations using Streamlit.
- 💾 Organized structure, reusable scripts, and production-ready code.

---

## 🗂️ Project Structure

```plaintext
Credit_Risk_Scoring_Model_with_Explainable_AI/
├── data/                # Generated .csv dataset
├── models/              # Trained LightGBM model
├── reports/             # Predictions and scores
├── visualizations/      # Confusion matrix plot
├── generate_credit_data.py     # Synthetic data generator
├── train_credit_model.py       # Model training and evaluation
├── score_client.py             # Interactive dashboard
├── simulate_score.py           # Risk score simulator
├── requirements.txt            # Required packages
└── README.md                   # Documentation
⚙️ Setup & Usage
1. Clone the repo and set up environment:

git clone https://github.com/warcklian/Credit_Risk_Scoring_Model_with_Explainable_AI.git
cd Credit_Risk_Scoring_Model_with_Explainable_AI
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
2. Run the pipeline:

python generate_credit_data.py       # Step 1: Generate data
python train_credit_model.py         # Step 2: Train model
streamlit run score_client.py        # Step 3: Dashboard
streamlit run simulate_score.py      # Optional: Simulator
📊 Model Evaluation Metrics
Metric	Description	Expected Value
AUC-ROC	Discrimination between risky and non-risky clients	> 0.70
Accuracy	Overall correct classification	> 0.75
Precision (1)	% of true defaults among predicted defaults	High
Recall (1)	% of actual defaults correctly identified	> 0.50
Confusion Matrix	Visual breakdown of prediction outcomes (TP, FP, TN, FN)	-

📦 Dependencies

Python >= 3.9

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
lightgbm
joblib
Install with:

pip install -r requirements.txt
📝 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests and feedback are welcome!
Fork the repo, create a feature branch, and submit a PR.

📅 Last updated: May 2025