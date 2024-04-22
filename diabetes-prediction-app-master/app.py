import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from typing import Tuple

st.set_page_config(layout="wide", page_title="Diabetes Prediction App", page_icon=":hospital:")

@st.cache
def load_model_and_scaler(scaler_path: str, model_path: str) -> Tuple:
    try:
        scaler = joblib.load(scaler_path)
        model = joblib.load(model_path)
        return scaler, model
    except FileNotFoundError:
        st.error("Model or scaler file not found. Please check the file paths.")
        return None, None

def make_inference(row: list, scaler, model, feature_columns: list) -> str:
    try:
        df = pd.DataFrame([row], columns=feature_columns)
        scaled_features = scaler.transform(df)
        prediction = model.predict(scaled_features)
        return "This person has a high chance of having diabetes." if prediction == 1 else "This is a healthy person!"
    except Exception as e:
        st.error(f"An error occurred during inference: {e}")
        return "Prediction error."

st.title('Diabetes Prediction App')
st.markdown("""
    Please note: This is a sample application and cannot be used as a substitute for real medical advice.
""")

st.sidebar.header("Input Patient Details")
age = st.sidebar.number_input("Age in Years", 1, 150, 25, 1)
pregnancies = st.sidebar.number_input("Number of Pregnancies", 0, 20, 0, 1)
glucose = st.sidebar.slider("Glucose Level", 0, 200, 25, 1)
skin_thickness = st.sidebar.slider("Skin Thickness", 0, 99, 20, 1)
blood_pressure = st.sidebar.slider('Blood Pressure', 0, 122, 69, 1)
insulin = st.sidebar.slider("Insulin", 0, 846, 79, 1)
bmi = st.sidebar.slider("BMI", 0.0, 67.1, 31.4, 0.1)
dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.000, 2.420, 0.471, 0.001)

if st.sidebar.button('Predict Health Status'):
    feature_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    scaler, model = load_model_and_scaler('scaler.joblib', 'model.joblib')

    if scaler and model:
        result = make_inference(row, scaler, model, feature_columns)
        st.subheader("Prediction Result:")
        st.write(result)

image = Image.open('./diabetes-prediction-app-master/data/diabetes_image.jpg') 
st.image(image, caption="Diabetes Prediction", use_column_width=True)

st.info("Note: This app is for educational purposes only and cannot be used as a substitute for professional medical advice.")

