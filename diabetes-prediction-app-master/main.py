import streamlit as st
from streamlit_option_menu import option_menu


import home, dashboard, prediction, recipe

st.set_page_config(
    page_title='PreDiabAlert - Early Diabetes Risk Calculator'
)

class MultiApp:
    
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='PreDiabAlert',
                options=['Home', 'Diabetes in Australia', 'Calculate Your Risk', 'Recommended Recipes'],
                icons=['info-circle-fill', 'bar-chart-steps', 'calculator-fill', 'hand-thumbs-up-fill'],
                menu_icon='house-fill',
                default_index=1,
                styles={
                    'container': {'padding': '5!important', 'background-color': '#48d1cc'}, #D0CFCF
                    'icon': {'color': '#2A2D34', 'font-size': '23px'}, 
                    'nav-link': {'color': 'black', 'font-size': '20px'},
                    'nav-link-selected': {'background-color': '#CCFF66'} #F1D302
                }
            )

        if app=='Home':
            home.app()
        if app=='Diabetes in Australia':
            dashboard.app()
            dashboard.dashboard()
        if app=='Calculate Your Risk':
            prediction.app()
            prediction.main()
           
        if app=='Recommended Recipes':
            recipe.gpt()
    run()
