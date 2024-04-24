import streamlit as st

def app():
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