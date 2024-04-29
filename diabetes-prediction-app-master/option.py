import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Assuming 'recipie_data.xlsx' exists with columns 'Recipies' and 'Meal'
excel_file = './diabetes-prediction-app-master/data/train.xlsx'

sheet_name = 'Sheet1'
df = pd.read_excel(excel_file, sheet_name=sheet_name, 
                   usecols=['Recipies', 'Meal', 'Details', 'Nutrition', 'Ingredients', 'Method', 'Image'])

def display_recipes(selected_meal, df):
    """Displays recipes based on the selected meal."""

    if selected_meal is not None:
        filtered_recipies = df[df['Recipies'] == selected_meal]
        selected_meal = st.selectbox("Choose a Recipie:", filtered_recipies['Meal'].unique())
        filtered_df = filtered_recipies[filtered_recipies['Meal'] == selected_meal]
        if not filtered_df.empty:
            #st.title(f"{filtered_recipies} ")
            #st.write(f"{selected_meal}")
            #st.image("https://www.diabetesaustralia.com.au/wp-content/uploads/baked-potato-with-tuna-and-salad-iStock-1219625655.png", width = 250)
            col1, col2 = st.columns(2)
            with col1:
                st.image(filtered_df["Image"].tolist(), width = 250)
            with col2:
                for index, row in filtered_df.iterrows():
                    #st.subheader(f"{row['Recipies']}")
                    st.subheader("Details:")
                    st.write(row["Details"])
            st.subheader("Ingredients:")
            st.text(row["Ingredients"])
            st.subheader("Instructions:")
            st.write(row["Method"])
        else:
            st.warning(f"No recipes found for {selected_meal}.")

with st.sidebar:
    selected_meal = option_menu(
        menu_title="Choose a Meal:",
        options=df['Recipies'].unique().tolist(),  # Use unique meals from DataFrame
        default_index=0  # Select the first option by default
    )
def main():
    st.title("Recipes App")
    display_recipes(selected_meal, df)  
    
if __name__ == '__main__':
    main() 
