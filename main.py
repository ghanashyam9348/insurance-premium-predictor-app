import streamlit as st
from prediction_helper import predict

# --- Page Setup ---
st.set_page_config(page_title="Insurance Premium Input UI", layout="centered")
st.title("🚑 Insurance Premium Predictor")
st.markdown("### Enter applicant details below:")

# --- Row 1: Age, Number of Dependents, Income in Lakhs ---
col1, col2, col3 = st.columns(3)
with col1:
    age = st.slider("Age", min_value=18, max_value=100, value=30)
with col2:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, step=1)
with col3:
    income_lakhs = st.number_input("Annual Income (in Lakhs)", min_value=0, step=1)

# --- Row 2: Income Level, Genetic Risk ---
col4, col5 = st.columns(2)
with col4:
    income_level = st.selectbox("Income Level", ['> 40L', '<10L', '10L - 25L', '25L - 40L'])
with col5:
    genetical_risk = st.number_input("Genetical Risk (0 to 10)", min_value=0, max_value=10, step=1)

# --- Row 3: Gender, Region, Marital Status ---
col6, col7, col8 = st.columns(3)
with col6:
    gender = st.selectbox("Gender", ['Male', 'Female'])
with col7:
    region = st.selectbox("Region", ['Northeast', 'Northwest', 'Southeast', 'Southwest'])
with col8:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

# --- Row 4: BMI, Smoking, Employment ---
col9, col10, col11 = st.columns(3)
with col9:
    bmi_category = st.selectbox("BMI Category", ['Overweight', 'Underweight', 'Normal', 'Obesity'])
with col10:
    smoking_status = st.selectbox("Smoking Status", [
        'Regular', 'No Smoking', 'Occasional', 'Smoking=0', 'Does Not Smoke', 'Not Smoking'
    ])
with col11:
    employment_status = st.selectbox("Employment Status", ['Self-Employed', 'Freelancer', 'Salaried'])

# --- Row 5: Insurance Plan & Medical History ---
col12, col13 = st.columns(2)
with col12:
    insurance_plan = st.selectbox("Insurance Plan", ['Silver', 'Bronze', 'Gold'])
with col13:
    medical_history = st.selectbox("Medical History", [
        'High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid',
        'Heart disease', 'Thyroid', 'High blood pressure & Heart disease'
    ], index=1)  # Default to 'No Disease'

# --- Collect Inputs ---
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# --- Predict Button ---
if st.button("Predict Insurance Premium"):
    prediction = predict(input_dict)

    st.markdown("---")
    st.markdown("### 🧾 Predicted Insurance Premium")

    # Display predicted value in a success box
    st.success(f"💰 Estimated Premium Amount: ₹ {prediction:,.2f}")
