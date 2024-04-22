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
    st.write('The data for the following example is originally from the National Institute of Diabetes and Digestive and Kidney Diseases and contains information on females at least 21 years old of Pima Indian heritage. This is a sample application and cannot be used as a substitute for real medical advice.')
    
    st.image('./diabetes-prediction-app-master/data/dataset-cover.png')
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
