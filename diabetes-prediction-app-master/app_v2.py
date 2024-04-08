import streamlit as st
import joblib
import pandas as pd
# from PIL import Image
# @st.cache_data
# def load(scaler_path, model_path):
#     sc = joblib.load(scaler_path)
#     model = joblib.load(model_path)
#     return sc , model

# def inference(row, scaler, model, feat_cols):
#     df = pd.DataFrame([row], columns = feat_cols)
#     X = scaler.transform(df)
#     features = pd.DataFrame(X, columns = feat_cols)
#     if (model.predict(features)==0):
#         return "This is a healthy person!"
#     else: return "This person has high chances of having diabetics!"
st.set_page_config(
            page_title="Diabetes Prediction App",
            page_icon= "🔍",
            layout="centered",
    )

tab1, tab2 = st.tabs(["📈 Diabetes in Australia", "🗃 Diabetes Prediction"])

with tab1:
    st.write('In this tab, we will demonstrate facts about diabetes and diabetes overview in Australia, using different kinds of illustrations. Some examples include:')
    st.markdown("- Maps to show regional variations in diabetes prevalence across Australia")
    st.markdown("- Charts to illustrate the distribution of diabetes cases by age group, gender, ethnicity, and type of diabetes")
    st.markdown("- Graph to depict trends in diabetes prevalence over time, showing how rates have changed in Australia over the years")
    
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)

with tab2:
    st.title('Diabetes Prediction App')
    st.write('The data for the following example is originally from the National Institute of Diabetes and Digestive and Kidney Diseases and contains information on females at least 21 years old of Pima Indian heritage. This is a sample application and cannot be used as a substitute for real medical advice.')
    
    st.image('dataset-cover.png', use_column_width=True)
    st.write('Please answer the below questions and click on the Submit button to generate the prediction!')
    
    gender = st.radio(
        'What is your gender?',
        options = ['Female', 'Male'])
    
    age = st.text_input("What is your age?")
    
    hypertension = st.radio(
        'Do you have hypertension?',
        options = ['Yes', 'No'])
    
    heart_disease = st.radio(
        'Do you have any heart disease?',
        options = ['Yes', 'No'])
    
    smoking_history = st.radio(
        'What is your smoking history?',
            options = ['Current', 'Never'])
    
    bmi = st.text_input("What is your BMI?")
    
    HbA1c_level = st.text_input("What is your HbA1c (glycated haemoglobin) blood test result?")
    
    blood_glucose_level = st.text_input("What is your blood glucose level?")

# row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

# if (st.button('Find Health Status')):
#     feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

#     sc, model = load('C:\\Users\\user\\Downloads\\Pictures\\diabetes-prediction-app-master\\diabetes-prediction-app-master\\models\\scaler.joblib',
#                  'C:\\Users\\user\\Downloads\\Pictures\\diabetes-prediction-app-master\\diabetes-prediction-app-master\\models\\model.joblib')

#     result = inference(row, sc, model, feat_cols)
#     st.write(result)
