import streamlit as st
import pandas as pd

def app():
    df = pd.read_csv('./data/Diabetes_Treatment_Options.csv')

    st.title('Diabetes Treatment Options')
    
    treatment_types = df['Treatment Type'].unique()
    selected_treatment_type = st.selectbox('Select Treatment Type:', treatment_types)
    
    filtered_df = df[df['Treatment Type'] == selected_treatment_type]
    
    for index, row in filtered_df.iterrows():
        with st.expander(f"{row['Action']} ({row['Condition']})"):
            st.write(f"**Details:** {row['Details']}")
