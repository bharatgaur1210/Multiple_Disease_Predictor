import streamlit as st
import numpy as np 
import pickle


st.title("Heart Disease Predictor")
st.subheader("A type of disease that affects the heart or blood vessels. The risk of certain heart diseases may be increased by high blood pressure, high cholesterol, unhealthy diet, lack of exercise, and obesity.")
st.subheader("The most common heart disease is coronary artery disease (narrow or blocked coronary arteries), which can lead to chest pain, heart attacks, or stroke.")
st.subheader("Other heart diseases include congestive heart failure, heart rhythm problems, congenital heart disease (heart disease at birth), and endocarditis (inflamed inner layer of the heart). Also called cardiovascular disease.")

# loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Desktop/MP/Sav_files/heart_trained.sav', 'rb'))

def heart_prediction(input_data):
    # Convert input strings to numeric values
    input_data_numeric = [float(x) for x in input_data]
    
    # Convert the list to a numpy array
    input_data_as_numpy_array = np.asarray(input_data_numeric)
    
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'THIS PERSON DOES NOT HAVE A HEALTHY HEART, NO CONSULTATION NEEDED'
    else:
        return 'THIS PERSON HAS A HEART CONDITION, CONSULT A DOCTOR IMMEDIATELY'

  
    
  
def main(): 
    
    age = st.text_input('Age of the person')
    sex = st.text_input('Gender of the person')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting blood pressure')
    chol = st.text_input('Serum cholesterol')
    fbs = st.text_input('Fasting blood sugar ')
    restecg = st.text_input('Resting electrocardiographic')
    thalach = st.text_input('Maximum heart rate achieved during exercise test')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('ST depression')
    slope = st.text_input('The slope of the peak exercise ST segment')
    ca = st.text_input('The number of major vessels')
    thal = st.text_input(' A blood disorder called thalassemia')
    
    
    
   
    diagnosis = ''
    
    
    
    if st.button('Heart Test Result'):
        diagnosis = heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ])
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()