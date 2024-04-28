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
    st.write('In this tab, we will demonstrate facts about diabetes and diabetes overview in Australia, using different kinds of illustrations. Some examples include:')

def dashboard():
    col1, col2 = st.columns(2)

    # Row 1, Column 1
    with col1:
        

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

        # Create DataFrame
        df = pd.DataFrame(data)

        # Set the index
        df.set_index("Age group", inplace=True)

        # Title
        st.title("Number of Individuals by Age Group and Gender")

        
        # Create an interactive chart
        selected_gender = st.selectbox("Select gender:", ["Males", "Females", "Persons"], key = 1)

        # Plot using Altair
        chart = alt.Chart(df.reset_index()).mark_bar().encode(
            x=alt.X("Age group", title="Age group"),
            y=alt.Y(selected_gender, title="Number of Individuals"),
            tooltip=["Age group", selected_gender]
        ).properties(
            title=f"Number of Individuals by Age Group ({selected_gender})"
        ).interactive()

        # Display the chart
        st.altair_chart(chart, use_container_width=True)
    
        

    # Row 1, Column 2
    with col2:
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
        st.title("Diabetes hospitalisations by age and sex")

        

        # Interactive chart using Altair
        selected_gender = st.selectbox("Select gender:", ["Males", "Females", "Persons"], key=2)

        # Plot using Altair
        chart = alt.Chart(df.reset_index()).mark_bar().encode(
            x=alt.X("Age group", title="Age group"),
            y=alt.Y(selected_gender, title="Number of Individuals"),
            tooltip=["Age group", selected_gender]
        ).properties(
            title=f"Number of Individuals by Age Group ({selected_gender})"
        ).interactive()

        # Display the chart
        st.altair_chart(chart, use_container_width=True)

    # Row 2, Column 1
    with col1:
        
            # Define the data
        data = {
            "Age group": [
                "0–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75–79", "80–84", "85+"
            ],
            "Males": [273, 260, 377, 590, 881, 1405, 1717, 2007, 3393],
            "Females": [186, 145, 197, 312, 475, 783, 981, 1414, 3869],
            "Persons": [459, 405, 574, 902, 1356, 2188, 2698, 3421, 7262]
        }

        # Create DataFrame
        df = pd.DataFrame(data)

        # Set the index
        df.set_index("Age group", inplace=True)

        # Title
        st.title("Interactive Pie Chart - Age Distribution by Gender")

    # Interactive pie chart using Altair
        selected_gender = st.selectbox("Select gender:", ["Males", "Females", "Persons"])

        # Calculate percentages for the selected gender
        total_selected_gender = df[selected_gender].sum()
        df["Percentage"] = (df[selected_gender] / total_selected_gender) * 100

        # Create Altair pie chart
        chart = alt.Chart(df.reset_index()).mark_arc().encode(
            theta=alt.Theta(field="Percentage", type="quantitative"),
            color=alt.Color("Age group:N", legend=alt.Legend(title="Age group")),
            tooltip=["Age group:N", "Percentage:Q"]
        ).properties(
            title=f"Age Distribution by {selected_gender}"
        )

        # Display the chart
        st.altair_chart(chart, use_container_width=True)

    # Row 2, Column 2
    with col2:    # Sample data (replace this with your actual data)
        data = {
            'Region': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'],
            'Latitude': [-33.8688, -37.8136, -27.4698, -31.9505, -34.9285],
            'Longitude': [151.2093, 144.9631, 153.0251, 115.8605, 138.6007],
            'Diabetes Prevalence (%)': [5.1, 4.9, 6.2, 4.5, 5.8]
        }

        # Create a DataFrame from the sample data
        df = pd.DataFrame(data)

        # Set up Streamlit app
        st.title('Diabetes Prevalence Map in Australia')

        # Create a base map centered around Australia
        map_center = [-25.2744, 133.7751]  # Coordinates for the center of Australia
        mymap = folium.Map(location=map_center, zoom_start=4)

        # Add markers to the map for each region
        marker_cluster = MarkerCluster().add_to(mymap)

        for i, row in df.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=f"<strong>{row['Region']}</strong><br>Diabetes Prevalence: {row['Diabetes Prevalence (%)']}%",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(marker_cluster)

        # Display the map using Streamlit
        st_folium(mymap, width=725, height=500)


