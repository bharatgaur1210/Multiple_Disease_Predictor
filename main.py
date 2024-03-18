import streamlit as st 
import pickle 
from sklearn import svm 
from sklearn.preprocessing import StandardScaler

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

from pages import diabetics, heart 

st.title("MULTIPLE DISEASE PREDICTOR")
st.subheader("Multiple disease predictor is a website that uses data analysis and machine learning to analyze a persons medical data and predict their risk of developing a particular disease.")

st.sidebar.title("About")
st.sidebar.markdown(
    """
    This application is developed using Streamlit, a powerful framework for building ML and data science web applications. It utilizes machine learning models to predict the risk of various diseases based on user input.
    """
)

# Add additional sections or information
st.header("How it Works")
st.markdown(
    """
    1. **Enter Your Medical Data**: Input relevant medical metrics such as age, gender, blood pressure, etc.
    2. **Get Predictions**: Click on the button to get predictions about the risk of developing a particular disease.
    3. **Take Action**: Based on the predictions, take appropriate actions such as consulting a doctor or making lifestyle changes.
    """
)

st.subheader("Information Section")
st.subheader("Heart")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("C:/Users/HP/Desktop/MP/images/heart.png", caption="Heart")
with col2:
    st.image("C:/Users/HP/Desktop/MP/images/risk_heart.png", caption="Risk Factors of Heart Disease")
with col3:
    st.image("C:/Users/HP/Desktop/MP/images/prevent_heart.png", caption="Prevention of Heart Disease")

st.subheader("Diabetics")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("C:/Users/HP/Desktop/MP/images/diabetic.png", caption="Diabetic")
with col2:
    st.image("C:/Users/HP/Desktop/MP/images/diabetic_risk.png", caption="Risk Factors of Diabetic Disease")
with col3:
    st.image("C:/Users/HP/Desktop/MP/images/diabetic_prevention.png", caption="Prevention of Diabetic Disease")

    

    
    





