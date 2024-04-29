import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
from streamlit_folium import st_folium


def app():
    st.title("Diabetes in Australia")
def dashboard():
   

    
        
        import plotly.express as px

        # Define the data
        data = {
            "Age group": [
                "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39",
                "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79",
                "80-84", "85+"
            ],
            "Males": [
                273, 1164, 2526, 3732, 5050, 6922, 10002, 16900, 25014, 36450,
                52585, 70235, 87319, 99230, 105684, 85945, 55324, 44466
            ],
            "Females": [
                282, 1110, 2521, 3637, 4835, 6870, 10442, 15371, 21012, 30777,
                45494, 58549, 70266, 76749, 79829, 67344, 50777, 53345
            ],
            "Persons": [
                555, 2274, 5047, 7369, 9904, 13796, 20446, 32273, 46029, 67231,
                98087, 128788, 157588, 175982, 185516, 153291, 106103, 97812
            ]
        }

        # Create a DataFrame from the data dictionary
        df = pd.DataFrame(data)

        # Streamlit app
        st.write('Population Distribution by Age Group')

        # Select the demographic group using a radio button
        selected_group = st.radio('Select Group:', ['Males', 'Females', 'Persons'])

        # Prepare data for the pie chart based on the selected group
        labels = df['Age group']
        values = df[selected_group]

        # Create an interactive pie chart using Plotly
        fig = px.pie(
            names=labels,
            values=values,
            title=f'Population Distribution by Age Group - {selected_group}',
            labels={'names': 'Age Group', 'values': 'Count'},
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        # Display the interactive pie chart
        st.plotly_chart(fig, use_container_width=True)

    
        

    # Row 1, Column 2
    
        data = {
        "Age group": [
            "0–4", "5–9", "10–14", "15–19", "20–24", "25–29", "30–34", "35–39",
            "40–44", "45–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75–79",
            "80–84", "85+"
        ],
        "Males": [
            301, 555, 1193, 1535, 2094, 3078, 4953, 8511, 12477, 21823,
            33911, 49093, 69683, 89277, 117006, 104554, 77534, 64647
        ],
        "Females": [
            263, 548, 1371, 3296, 9504, 21900, 33916, 28805, 18705, 22308,
            28980, 39291, 50067, 63036, 76585, 68045, 59521, 62461
        ],
        "Persons": [
            564, 1103, 2564, 4836, 11606, 24980, 38872, 37322, 31183, 44133,
            62893, 88384, 119751, 152315, 193601, 172601, 137056, 127109
        ]
    }

        # Create DataFrame
        df = pd.DataFrame(data)

        # Set the index
        df.set_index("Age group", inplace=True)

        # Title
        st.write("Diabetes hospitalisations by age and sex")

        

        # Interactive chart using Altair
        selected_gender = st.selectbox("Select gender:", ["Males", "Females", "Persons"], key=2)

        # Plot using Altair
        chart = alt.Chart(df.reset_index()).mark_bar().encode(
            x=alt.X("Age group", title="Age group"),
            y=alt.Y(selected_gender, title="Number of Individuals"),
            tooltip=["Age group", selected_gender]
        ).properties(
            title=f"Diabetes hospitalisations ({selected_gender})"
        ).interactive()

        # Display the chart
        st.altair_chart(chart, use_container_width=True)

    # Row 2, Column 1
   
            

    # Row 2, Column 2
      # Sample data (replace this with your actual data)
      
        import plotly.express as px

        # Define the data (replace this with your actual dataset)
        data = {
            'Year': [
                2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
            ],
            'Males': [
                5381, 5612, 6225, 6069, 6254, 6325, 6805, 7011, 7721, 7625,
                7685, 8184, 8116, 8218, 8493, 9016, 9457, 9876, 9825, 10010, 10256, 10903
            ],
            'Females': [
                4749, 4713, 5242, 5331, 5481, 5539, 6044, 6127, 6718, 6673,
                6664, 6928, 6984, 6979, 7341, 7543, 7651, 7892, 7620, 7789, 7766, 8363
            ],
            'Persons': [
                10130, 10325, 11467, 11400, 11735, 11864, 12849, 13138, 14439, 14298,
                14349, 15112, 15100, 15197, 15834, 16559, 17108, 17768, 17445, 17799, 18022, 19266
            ]
        }

        df = pd.DataFrame(data)

        # Streamlit app
        st.write('Diabetes Prevalence Over Time (2000-2021)')

    

        # Create an interactive time series chart using Plotly
        fig = px.line(df, x='Year', y=['Males', 'Females', 'Persons'], title='Diabetes Prevalence Over Time (2000-2021)')
        st.plotly_chart(fig)

        
        st.image('./diabetes-prediction-app-master/data/chart.png', use_column_width=True)




