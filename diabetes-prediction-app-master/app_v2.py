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

tab1, tab2, tab3 = st.tabs(["📈 Diabetes in Australia", "🗃 Diabetes Prediction","Recipe"])

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
        st.title('Diabetes Prediction App')
        model = load_model()

        # Order of features as specified
        feature_columns = [
            'age', 'polyuria', 'polydipsia', 'sudden_weight_loss', 'weakness',
            'polyphagia', 'genital_thrush', 'visual_blurring', 'itching',
            'irritability', 'delayed_healing', 'partial_paresis', 'muscle_stiffness',
            'alopecia', 'obesity', 'gender_Female', 'gender_Male'
        ]

        with st.form("diabetes_prediction_form"):
            st.write("Please enter the following details:")
            age = st.number_input('Age', min_value=0, max_value=120, value=30)
            # Map 'Yes'/'No' answers to 1/0 and add inputs for all other features
            polyuria = st.radio('Polyuria', ['Yes', 'No'], format_func=lambda choice: choice)
            polydipsia = st.radio('Polydipsia', ['Yes', 'No'], format_func=lambda choice: choice)
            sudden_weight_loss = st.radio('Sudden Weight Loss', ['Yes', 'No'], format_func=lambda choice: choice)
            weakness = st.radio('Weakness', ['Yes', 'No'], format_func=lambda choice: choice)
            polyphagia = st.radio('Polyphagia', ['Yes', 'No'], format_func=lambda choice: choice)
            genital_thrush = st.radio('Genital Thrush', ['Yes', 'No'], format_func=lambda choice: choice)
            visual_blurring = st.radio('Visual Blurring', ['Yes', 'No'], format_func=lambda choice: choice)
            itching = st.radio('Itching', ['Yes', 'No'], format_func=lambda choice: choice)
            irritability = st.radio('Irritability', ['Yes', 'No'], format_func=lambda choice: choice)
            delayed_healing = st.radio('Delayed Healing', ['Yes', 'No'], format_func=lambda choice: choice)
            partial_paresis = st.radio('Partial Paresis', ['Yes', 'No'], format_func=lambda choice: choice)
            muscle_stiffness = st.radio('Muscle Stiffness', ['Yes', 'No'], format_func=lambda choice: choice)
            alopecia = st.radio('Alopecia', ['Yes', 'No'], format_func=lambda choice: choice)
            obesity = st.radio('Obesity', ['Yes', 'No'], format_func=lambda choice: choice)
            gender = st.selectbox('Gender', ['Female', 'Male'])

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
    
with tab3:
    excel_file = './diabetes-prediction-app-master/data/recipie_data.xlsx'
    sheet_name = 'Sheet1'

    df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:F')


    def recipe_section():
        st.header("Recipes")
        if 'Recipies' in df.columns:
            # Get unique recipe names
            unique_recipes = df['Recipies'].unique()
            cols = st.columns(len(unique_recipes))  # Create columns for tiles

            # Use session state to store selected recipe
            if 'selected_recipe' not in st.session_state:
                st.session_state['selected_recipe'] = None

            selected_recipe = st.session_state['selected_recipe']  # Get from session state

            # Use a flag to track tile clicks
            recipe_clicked = False

            for i, recipe in enumerate(unique_recipes):
                if cols[i].button(recipe):
                    selected_recipe = recipe
                    recipe_clicked = True  # Set flag if clicked
                    break  # Exit loop after first click

            # Update session state only if a new recipe was clicked
            if recipe_clicked:
                st.session_state['selected_recipe'] = selected_recipe

            if selected_recipe is not None:
                # Filter meals based on selected recipe (check for 'Meal' column)
                if 'Meal' in df.columns:
                    filtered_meals = df[df['Recipies'] == selected_recipe]['Meal'].unique()

                    if len(filtered_meals) > 0:
                        # Choose meal if there are options
                        selected_meal = st.selectbox("Choose a Meal:", filtered_meals)
                        # Display recipe details based on selected recipe and meal
                        filtered_df = df[(df['Recipies'] == selected_recipe) & (df['Meal'] == selected_meal)]
                        display_recipe_details(filtered_df)
                    else:
                        st.warning(f"No meal options found for {selected_recipe}.")
                else:
                    st.warning("No 'Meal' column found. Skipping meal selection.")
                    filtered_df = df[df['Recipies'] == selected_recipe]
                    display_recipe_details(filtered_df)
            else:
                st.info("Please select a recipe tile.")


    def display_recipe_details(df):
        if not df.empty:
            for index, row in df.iterrows():
                st.subheader(f"{row['Recipies']}")
                st.write("Details:")
                st.text(row["Details"])
                st.write("Ingredients:")
                st.text(row["Ingredients"])
                st.write("Instructions:")
                st.text(row["Method"])
        else:
            st.warning(f"No details found for selected recipe.")


    def main():
        st.title("Recipes App")
        recipe_section()


    if __name__ == '__main__':
        main() 

# row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

# if (st.button('Find Health Status')):
#     feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

#     sc, model = load('C:\\Users\\user\\Downloads\\Pictures\\diabetes-prediction-app-master\\diabetes-prediction-app-master\\models\\scaler.joblib',
#                  'C:\\Users\\user\\Downloads\\Pictures\\diabetes-prediction-app-master\\diabetes-prediction-app-master\\models\\model.joblib')

#     result = inference(row, sc, model, feat_cols)
#     st.write(result)
