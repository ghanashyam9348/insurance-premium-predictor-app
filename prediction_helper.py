import pandas as pd
from joblib import load

# Load models
model_rest = load("artifacts/model_rest.joblib")
model_young = load("artifacts/model_young.joblib")

# Load scalers
scaler_rest = load("artifacts/scaler_rest.joblib")
scaler_young = load("artifacts/scaler_young.joblib")


def calculate_risk_score(medical_history):
    """
    Calculate normalized risk score based on medical history string.
    """
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    diseases = medical_history.lower().split(" & ")

    if len(diseases) == 1:
        diseases.append("none")

    disease1 = diseases[0].strip()
    disease2 = diseases[1].strip()

    score1 = risk_scores.get(disease1, 0)
    score2 = risk_scores.get(disease2, 0)

    total_score = score1 + score2
    normalized_score = total_score / 14  # Max possible risk score is 14

    return normalized_score


def handle_scaling(age, df):
    """
    Scale numerical columns using appropriate scaler based on age group.
    Keeps 'income_level' placeholder as per user logic, and drops it after scaling.
    """
    scaler_object = scaler_young if age <= 25 else scaler_rest
    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None  # Placeholder column to satisfy structure
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis='columns', inplace=True)

    return df


def preprocess_input(input_dict):
    """
    Convert input_dict from UI into a model-ready DataFrame.
    Includes numerical fields, one-hot encoding, and risk score calculation.
    """
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
        'genetical_risk', 'normalized_risk_score', 'gender_Male',
        'region_Northwest', 'region_Southeast', 'region_Southwest',
        'marital_status_Unmarried', 'bmi_category_Obesity',
        'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # --- Assign numerical features ---
    df.loc[0, 'age'] = input_dict['Age']
    df.loc[0, 'number_of_dependants'] = input_dict['Number of Dependants']
    df.loc[0, 'income_lakhs'] = input_dict['Income in Lakhs']
    df.loc[0, 'genetical_risk'] = input_dict['Genetical Risk']

    # Encode insurance plan numerically
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    df.loc[0, 'insurance_plan'] = insurance_plan_encoding.get(input_dict['Insurance Plan'], 0)

    # --- One-hot encodings ---
    if input_dict['Gender'] == 'Male':
        df.loc[0, 'gender_Male'] = 1

    region = input_dict['Region']
    if region == 'Northwest':
        df.loc[0, 'region_Northwest'] = 1
    elif region == 'Southeast':
        df.loc[0, 'region_Southeast'] = 1
    elif region == 'Southwest':
        df.loc[0, 'region_Southwest'] = 1

    if input_dict['Marital Status'] == 'Unmarried':
        df.loc[0, 'marital_status_Unmarried'] = 1

    bmi = input_dict['BMI Category']
    if bmi == 'Obesity':
        df.loc[0, 'bmi_category_Obesity'] = 1
    elif bmi == 'Overweight':
        df.loc[0, 'bmi_category_Overweight'] = 1
    elif bmi == 'Underweight':
        df.loc[0, 'bmi_category_Underweight'] = 1

    smoking = input_dict['Smoking Status']
    if smoking == 'Regular':
        df.loc[0, 'smoking_status_Regular'] = 1
    elif smoking == 'Occasional':
        df.loc[0, 'smoking_status_Occasional'] = 1

    employment = input_dict['Employment Status']
    if employment == 'Salaried':
        df.loc[0, 'employment_status_Salaried'] = 1
    elif employment == 'Self-Employed':
        df.loc[0, 'employment_status_Self-Employed'] = 1

    # --- Risk Score ---
    df.loc[0, 'normalized_risk_score'] = calculate_risk_score(input_dict['Medical History'])

    # --- Scaling ---
    df = handle_scaling(input_dict['Age'], df)

    return df


def predict(input_dict):
    """
    Perform prediction using pre-trained models based on applicant age group.
    """
    input_df = preprocess_input(input_dict)
    model = model_young if input_dict['Age'] <= 25 else model_rest
    prediction = model.predict(input_df)
    return int(prediction)
