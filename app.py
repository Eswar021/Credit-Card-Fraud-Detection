import streamlit as st
import pickle
import numpy as np

# Load the model
with open('Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Credit Card Fraud Detection")

st.write("Enter the transaction details to predict whether it's fraudulent or not.")

# Create input fields for the 30 features
inputs = []
for i in range(30):
    inputs.append(st.number_input(f"Feature {i+1}", value=0.0))

print("inputs are ------", inputs)
# Convert input to numpy array
input_array = np.array(inputs).reshape(1, -1)

print("converted are inputs are ------",input_array)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_array)
    
    if prediction[0] == 1:
        st.error("This transaction is likely fraudulent.")
    else:
        st.success("This transaction is likely not fraudulent.")

# Run the app with: streamlit run app.py
