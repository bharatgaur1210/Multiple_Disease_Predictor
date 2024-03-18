import streamlit as st 
import numpy as np
from sklearn import svm 
from sklearn.preprocessing import StandardScaler
import pickle 

st.title("Diabetics Disease Predictor")
st.subheader("Diabetes usually refers to diabetes mellitus in which there is also a high level of glucose (a type of sugar) in the blood because the body does not make enough insulin or use it the way it should.")
st.subheader("Hyperglycaemia, also called raised blood glucose or raised blood sugar, is a common effect of uncontrolled diabetes and over time leads to serious damage to many of the body's systems, especially the nerves and blood vessels.")

# loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Desktop/MP/Sav_files/diabetic_trained.sav', 'rb'))
scaler = pickle.load(open('C:/Users/HP/Desktop/MP/Sav_files/scalar.sav', 'rb')) 

def diabetes_prediction(input_data):
   
    input_data_numeric = [float(x) for x in input_data]
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    std_data = scaler.transform(input_data_reshaped)
    print(std_data)

    prediction = loaded_model.predict(std_data)
    print(prediction)

    if (prediction[0] == 1):
      return 'The person is diabetic'
    else:
      return 'The person is not diabetic'
  
    
  
def main(): 
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
