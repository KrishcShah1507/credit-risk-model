# 🏦 Credit Risk Modeling with XGBoost

This project predicts the likelihood of a loan default using historical LendingClub data and an XGBoost model. It includes a machine learning pipeline and an interactive Streamlit web interface for users to test inputs.

---

## 📌 Features

- Binary classification: **Default / No Default**
- Trained using LendingClub dataset
- Uses **XGBoost**, **Logistic Regression**
- SHAP analysis for model explainability (optional)
- **Streamlit app** for real-time predictions
- Deployed locally (or deployable to Streamlit Cloud)

---

## 📁 Project Structure

credit-risk-model/
├── Credit_Risk_Model.ipynb # Colab notebook used for training
├── app.py # Streamlit web app
├── model.pkl # Trained XGBoost model
├── requirements.txt # Required Python packages
└── README.md # Project description

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KrishcShah1507/credit-risk-model.git
cd credit-risk-model

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

🧠 Model Details
Trained using XGBoostClassifier

32 numerical/categorical engineered features

Categorical features encoded

Missing values imputed

Saved as model.pkl for reuse in the app

📌 To Do / Future Enhancements
✅ Add more features for better accuracy

✅ Include SHAP values for explainability

⏳ Add database integration for storing predictions
⏳ Add user login system
⏳ Deploy on Render or Heroku

👨‍💻 Author
Krish Shah
https://www.linkedin.com/in/krish-shah-b98551311/
https://github.com/KrishcShah1507

