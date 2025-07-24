import streamlit as st
import numpy as np
import joblib

model = joblib.load('Model/ML_Model1.pkl')  

st.title("🏦 Bank Loan Prediction App")

st.subheader("Enter Applicant Details")
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0
Property_Area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[Property_Area]
Dependents = 3 if Dependents == "3+" else int(Dependents)


features = np.array([[Gender, Married, Dependents, Education,
                      Self_Employed, ApplicantIncome, CoapplicantIncome,
                      LoanAmount, Loan_Amount_Term, Credit_History,
                      Property_Area]])


if st.button("Predict Loan Approval"):
    prediction = model.predict(features)
    result = "✅ Loan Approved" if prediction[0] == 'Y' else "❌ Loan Rejected"
    st.success(f"Prediction: {result}")
