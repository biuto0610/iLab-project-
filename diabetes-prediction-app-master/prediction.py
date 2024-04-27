import streamlit as st
import joblib
from joblib import load
import pandas as pd

def app():
    st.title('Diabetes Prediction App')
    st.write('Diabetes is one of the fastest growing chronic life threatening diseases that have already affected 422 million people worldwide according to the report of World Health Organization (WHO), in 2018. Due to the presence of a relatively long asymptomatic phase, early detection of diabetes is always desired for a clinically meaningful outcome. Around 50% of all people suffering from diabetes are undiagnosed because of its long-term asymptomatic phase.')
    
    st.image('./diabetes-prediction-app-master/data/dataset-cover.png')
    st.write('Please answer the below questions and click on the Submit button to generate the prediction!')
    
def load_model():
        # Assuming the model is pre-trained and saved as 'random_forest_model.pkl'
        return joblib.load('./diabetes-prediction-app-master/models/random_forest_model.pkl')

def predict_diabetes(input_data, feature_columns):
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        input_df = pd.get_dummies(input_df)

        # Ensure all expected feature columns are present in the DataFrame
        missing_cols = set(feature_columns) - set(input_df.columns)
        for c in missing_cols:
            input_df[c] = 0  # Add missing columns with default value of 0

        # Ensure the order of column names matches the order during model training
        input_df = input_df[feature_columns]

        # Load model and predict
        model = load_model()
        probability = model.predict_proba(input_df)[0][1]  # [0][1] to get the probability for the positive class
        return probability

def main():
    model = load_model()

        # Order of features as specified
    feature_columns = [
            'age', 'polyuria', 'polydipsia', 'sudden_weight_loss', 'weakness',
            'polyphagia', 'genital_thrush', 'visual_blurring', 'itching',
            'irritability', 'delayed_healing', 'partial_paresis', 'muscle_stiffness',
            'alopecia', 'obesity', 'gender_Female', 'gender_Male'
        ]

    with st.form("diabetes_prediction_form"):
            age = st.number_input('How old are you?', min_value=0, max_value=120, value=30)
            polyuria = st.radio('Do you urinate more frequently than usual?', ['Yes', 'No'])
            polydipsia = st.radio('Do you often feel very thirsty?', ['Yes', 'No'])
            sudden_weight_loss = st.radio('Have you lost a lot of weight suddenly without trying?', ['Yes', 'No'])
            weakness = st.radio('Do you often feel very weak?', ['Yes', 'No'])
            polyphagia = st.radio('Do you often feel hungrier than usual?', ['Yes', 'No'])
            genital_thrush = st.radio('Have you had fungal infections around the genital area?', ['Yes', 'No'])
            visual_blurring = st.radio('Do you find your vision blurring occasionally?', ['Yes', 'No'])
            itching = st.radio('Do you often feel itchy?', ['Yes', 'No'])
            irritability = st.radio('Have you been feeling unusually irritable?', ['Yes', 'No'])
            delayed_healing = st.radio('Do cuts or bruises heal slowly on your body?', ['Yes', 'No'])
            partial_paresis = st.radio('Do you experience weakness in your limbs?', ['Yes', 'No'])
            muscle_stiffness = st.radio('Do your muscles feel stiff regularly?', ['Yes', 'No'])
            alopecia = st.radio('Have you noticed significant hair loss recently?', ['Yes', 'No'])
            obesity = st.radio('Would you consider yourself to be obese?', ['Yes', 'No'])
            gender = st.selectbox('What is your gender?', ['Female', 'Male'])

            # Create the input dictionary according to the specified feature order
            input_data = {
                'age': age,
                'polyuria': 1 if polyuria == 'Yes' else 0,
                'polydipsia': 1 if polydipsia == 'Yes' else 0,
                'sudden_weight_loss': 1 if sudden_weight_loss == 'Yes' else 0,
                'weakness': 1 if weakness == 'Yes' else 0,
                'polyphagia': 1 if polyphagia == 'Yes' else 0,
                'genital_thrush': 1 if genital_thrush == 'Yes' else 0,
                'visual_blurring': 1 if visual_blurring == 'Yes' else 0,
                'itching': 1 if itching == 'Yes' else 0,
                'irritability': 1 if irritability == 'Yes' else 0,
                'delayed_healing': 1 if delayed_healing == 'Yes' else 0,
                'partial_paresis': 1 if partial_paresis == 'Yes' else 0,
                'muscle_stiffness': 1 if muscle_stiffness == 'Yes' else 0,
                'alopecia': 1 if alopecia == 'Yes' else 0,
                'obesity': 1 if obesity == 'Yes' else 0,
                'gender_Female': 1 if gender == 'Female' else 0,
                'gender_Male': 1 if gender == 'Male' else 0,
            }

            submit_button = st.form_submit_button("Predict Diabetes")
            if submit_button:
                probability = predict_diabetes(input_data, feature_columns)
                st.write(f'The probability of diabetes is {probability:.2%}')

    if __name__ == "__main__":
        main()
