import streamlit as st
import pandas as pd
import openai
from streamlit_chat import message

def header(url):
     st.markdown(f'<p style="background-color:white;color:#4DB5B5;font-size:40px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
excel_file = './diabetes-prediction-app-master/data/train.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:G')
    
def recipe_section():
    st.header("Recipes for healthy meal and snack")
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
        col1, col2 = st.columns(2)
        with col1:
            st.image(df["Image"].tolist(), width=250)
        with col2:
            for index, row in df.iterrows():
                st.subheader("Details:")
                st.write(row["Details"])
        st.subheader("Ingredients:")
        st.text(row["Ingredients"])
        st.subheader("Instructions:")
        st.write(row["Method"])
    else:
        st.warning(f"No details found for selected recipe.")

def main():
        recipe_section()


if __name__ == '__main__':
        main() 






