# Diabetes Prediction App [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/arunnthevapalan/diabetes-prediction-app/app.py)
Streamlit Web App to predict the early risk of diabetes based on diagnostic measures. 

## Data

The data is [available on Kaggle.]([https://www.kaggle.com/uciml/pima-indians-diabetes-database](https://www.kaggle.com/datasets/andrewmvd/early-diabetes-classification?resource=download)) The data contains 520 observations with 17 characteristics, collected using direct questionnaires and diagnosis results from the patients in the Sylhet Diabetes Hospital in Sylhet, Bangladesh.

## Pre-requisites

The project was developed using python 3.6.7 with the following packages.
- Pandas
- Numpy
- Scikit-learn
- Pandas-profiling(renamed as ydata_profiling)
- Joblib
- Streamlit

Installation with pip:

```bash
pip install -r requirements.txt
```

## Getting Started
Open the terminal in you machine and run the following command to access the web application in your localhost.
```bash
streamlit run main.py
```

## Files
- diabetes_prediction_pipeline.ipynb : Jupyter Notebook with all the workings including pre-processing, modelling and inference.
- main.py : Streamlit App script
- requirements.txt : pre-requiste libraries for the project
- models/ : trained model files and scaler objects
- data/ : source data

## Acknowledgements

[Kaggle](https://kaggle.com/), for providing the data for the machine learning pipeline.  
[Streamlit](https://www.streamlit.io/), for the open-source library for rapid prototyping.



