import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("xgboost_credit_model.pkl")

st.title("Credit Risk Prediction App")
st.write("Enter the details below to predict loan default risk:")

# Example input fields (customize as per your dataset)
income = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_score = st.number_input("Credit Score", min_value=0, max_value=850)

# When the user clicks the Predict button
if st.button("Predict"):
    input_data = np.array([[income, loan_amount, credit_score]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ High risk: Likely to default.")
    else:
        st.success("✅ Low risk: Likely to repay.")
