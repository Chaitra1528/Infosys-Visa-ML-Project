import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="Visa Processing Time Estimator", layout="centered")

st.title("Visa Processing Time Estimator")
st.write("This tool predicts visa processing time based on applicant details.")

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "visa_model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

# Inputs
age = st.number_input("Age", min_value=18, max_value=80, value=25)
documents = st.number_input("Documents Submitted", min_value=1, max_value=9, value=3)
visa_granted = st.selectbox("Visa Granted", ["Yes", "No"])

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "age": age,
        "documents_submitted_Bank Statement": 1 if documents >= 1 else 0,
        "documents_submitted_Medical Certificate": 1 if documents >= 2 else 0,
        "documents_submitted_English Proficiency": 1 if documents >= 3 else 0,
        "documents_submitted_Birth Certificate": 1 if documents >= 4 else 0,
        "documents_submitted_Police Clearance": 1 if documents >= 5 else 0,
        "documents_submitted_Work Experience Letters": 1 if documents >= 6 else 0,
        "documents_submitted_Travel Insurance": 1 if documents >= 7 else 0,
        "documents_submitted_Itinerary": 1 if documents >= 8 else 0,
        "documents_submitted_Invitation Letter": 1 if documents >= 9 else 0,
        "visa_granted_Yes": 1 if visa_granted == "Yes" else 0
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Processing Time: {int(prediction[0])} days")
