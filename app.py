import streamlit as st
import pickle
import numpy as np
import os
import subprocess

# Check if required libraries are installed
def install_requirements():
    if not os.path.exists('requirements.txt'):
        st.error("requirements.txt file not found. Please add it to the project directory.")
        return

# Ensure the environment has required packages
install_requirements()

# Load the model
try:
    with open('Model.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Failed to load the model: {str(e)}")
    st.stop()

# Define the Streamlit app
st.title("Credit Card Fraud Detection")

st.write("Enter the transaction details to predict whether it's fraudulent or not.")

# Create input fields for the 30 features
inputs = []
for i in range(30):
    inputs.append(st.number_input(f"Feature {i+1}", value=0.0))

# Convert input to numpy array
input_array = np.array(inputs).reshape(1, -1)

# Predict button
if st.button("Predict"):
    try:
        prediction = model.predict(input_array)
        if prediction[0] == 1:
            st.error("This transaction is likely fraudulent.")
        else:
            st.success("This transaction is likely not fraudulent.")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
