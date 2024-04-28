import streamlit as st

def header(url):
     st.markdown(f'<p style="background-color:white;color:#4DB5B5;font-size:40px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

def write(url):
     st.markdown(f'<p style="background-color:white;color:black;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

def app():
    header('About the Project')
    st.divider()
    write("""Welcome to PreDiabAlert App, your proactive health companion ✨.""") 
    write("""Our mission is to empower individuals with the tools they need to manage their health effectively, starting with the early detection of diabetes.""")
    write("""Diabetes is a growing global concern, and early symptoms can often be subtle and easily overlooked. Our app uses advanced data science techniques to predict the probability of developing diabetes based on these early signs. By identifying risks early, we aim to provide users with the opportunity to make informed lifestyle changes and seek medical advice promptly.""")
    write("""But we do not just stop at detection. PreDiabAlert App also offers personalized recipe recommendations designed to help maintain a healthy diet. These recipes are tailored to your dietary needs and preferences, supporting you in your journey towards a healthier life.""")
    write("""Join us in taking a proactive approach to health. With PreDiabAlert App, you are not just monitoring your health; you are actively improving it.""")

    header('About the Team')
    st.divider()    
    st.image('./diabetes-prediction-app-master/data/group pic(2).png') 
