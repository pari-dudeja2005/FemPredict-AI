import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('pcos_rf_model.pkl') 
st.set_page_config(page_title="Predict PCOS", page_icon="Fempredictlogo.png", layout="centered")

# Display logo at the top
st.image("Fempredictlogo.png", width=300)  

# Function to make predictions
def predict_pcos(user_data):
   
   
    prediction = model.predict(user_data)[0]
    
    return prediction

# Streamlit app layout
st.title('Predict PCOS')

# Collect user input using Streamlit widgets
age = st.number_input("Age (in years):", min_value=18, max_value=100, step=1)
weight = st.number_input("Weight (in kg):", min_value=30, max_value=200, step=1)
height = st.number_input("Height (in cm):", min_value=100, max_value=250, step=1)

# Blood group dropdown
blood_groups = {
    "A+": 11,
    "A-": 12,
    "B+": 13,
    "B-": 14,
    "O+": 15,
    "O-": 16,
    "AB+": 17,
    "AB-": 18
}
blood_group = st.selectbox("Select Blood Group", options=list(blood_groups.keys()))

# Map selected blood group to its numeric value
blood_group_value = blood_groups[blood_group]

# Period Frequency radio button
period_freq = st.radio("Period Frequency:", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Irregular")

# Yes/No radio buttons
weight_gain = st.radio("Have you gained weight recently?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
hair_growth = st.radio("Do you have excessive body/facial hair growth?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
skin_darkening = st.radio("Are you noticing skin darkening recently?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
hair_loss = st.radio("Do you have hair loss/hair thinning/baldness?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
acne = st.radio("Do you have pimples/acne on your face/jawline?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
fast_food = st.radio("Do you eat fast food regularly?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
exercise = st.radio("Do you exercise on a regular basis?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
mood_swings = st.radio("Do you experience mood swings?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
regular_periods = st.radio("Are your periods regular?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Period length input
period_length = st.number_input("How long does your period last? (in Days):", min_value=1, max_value=7, step=1)

# Create the user input array (converted to numerical format as needed)
user_data = np.array([[age, weight, height, blood_group_value, period_freq, weight_gain, hair_growth,
                       skin_darkening, hair_loss, acne, fast_food, exercise,
                       mood_swings, regular_periods, period_length]])

# When the user presses the "Predict" button
if st.button('Predict'):
    try:
        # Make prediction
        prediction = predict_pcos(user_data)
        
        # Display the result
        if prediction == 1:
            st.success("The model predicts that you may have PCOS. Please consult a healthcare professional for further evaluation.")
        else:
            st.success("The model predicts that you are unlikely to have PCOS. However, it is always good to consult a healthcare professional for personalized advice.")
    
    except Exception as e:
        st.error(f"Error: {e}")
