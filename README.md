# 🏦 Loan Prediction ML Project

This project predicts whether a loan will be approved or not based on various applicant details using Machine Learning.

## 📁 Project Structure
```
Loan-Prediction-Project/
├── app.py # Streamlit App
├── models/
│ └── final_model.pkl # Trained ML model
├── merged_data.csv
├── notebook.ipynb # Jupyter notebook (EDA + model training)
├── Requirements.txt 
└── README.md # Project description
```


## 🧠 Problem Statement

The goal is to build a machine learning model that predicts whether a loan application will be approved based on the applicant’s information.

## 🔍 Features Used

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

## ✅ Target Variable

- **Loan_Status**: 'Y' (Yes - Approved), 'N' (No - Rejected)

## 🛠️ ML Models Used

- Logistic Regression
- Decision Tree

## 💡 Steps Followed

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering & Selection
4. Model Training & Evaluation
5. Model Saving (.pkl)
6. Web App using Streamlit

## ✍️ Team Members
   
VIDHYALAKSHMI RV

SANDHIYA S

DIVYA K

ZABIULLA

## 🚀 How to Run the App

```bash
streamlit run app.py
