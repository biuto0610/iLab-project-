import streamlit as st
import pandas as pd

def app():
    excel_file = './data/recipie_data.xlsx'
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