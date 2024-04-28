import streamlit as st
import pandas as pd
import openai
from streamlit_chat import message


excel_file = './diabetes-prediction-app-master/data/recipie_data.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:F')

def chat_with_bot(user_input):
    try:
        # Start the OpenAI call
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150,  # Limit tokens to manage response lengths
            temperature=0.7,  # Adjust temperature to tweak randomness
        )
        # Extract the text of the response
        bot_response = response.choices[0].text.strip()
        return bot_response
    except Exception as e:
        # Handle exceptions and return an error message
        print(f"An error occurred: {e}")
        return "I'm sorry, I couldn't fetch a response. Please try again."
def on_send():
    user_input = st.session_state.user_input  # Get the current value of the text input
    if user_input:
        # Get the bot's response
        bot_response = chat_with_bot(user_input)

        # Update chat history
        st.session_state.chat_history.append({"message": user_input, "is_user": True})
        st.session_state.chat_history.append({"message": bot_response, "is_user": False})

        # Clear input field
        st.session_state.user_input = ""
    
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
def gpt():
    st.title("Diabetes-Friendly Recipes and Chatbot")

    tab1, tab2 = st.tabs(["Recipe", "Chat with Diabetes bot"])
    with tab2:
        st.header("Chatbot")
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []

        user_input = st.text_input("You: ", key="user_input", on_change=on_send)
        st.button("Send", on_click=on_send)

        for chat in reversed(st.session_state.chat_history):
            message(chat["message"], is_user=chat["is_user"], key=chat["message"])

    with tab1:
        recipe_section()

def main():
        st.title("Recipes App")
        recipe_section()


if __name__ == '__main__':
        main() 






