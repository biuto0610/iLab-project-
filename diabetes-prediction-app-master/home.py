import streamlit as st

def app():
    st.header('About the Team')
    st.image('./diabetes-prediction-app-master/data/group pic.png')
    st.header('About the Project')
    st.write("""
Welcome to Diabetes Prediction App, your proactive health companion. Our mission is to empower individuals with the tools they need to manage their health effectively, starting with the early detection of diabetes.

Diabetes is a growing global concern, and early symptoms can often be subtle and easily overlooked. Our app uses advanced data science techniques to predict the probability of developing diabetes based on these early signs. By identifying risks early, we aim to provide users with the opportunity to make informed lifestyle changes and seek medical advice promptly.

But we don’t just stop at detection. [App Name] also offers personalized recipe recommendations designed to help maintain a healthy diet. These recipes are tailored to your dietary needs and preferences, supporting you in your journey towards a healthier life.

Join us in taking a proactive approach to health. With Diabetes Prediction App, you’re not just monitoring your health; you're actively improving it.""")