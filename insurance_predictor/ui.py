import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox('Occupation',['Retired','Freelancer','Student','Governement_job','Buisness_owner','Unemployed','Private_job'])

if st.button('Predict premium category'):
    # 1. Complete the dictionary mapping
    input_data = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occupation': occupation
    }
    
    # 2. Add a visual loading spinner for better user experience
    with st.spinner("Analyzing profile..."):
        try:
            # 3. Send the POST request to your FastAPI server
            response = requests.post(API_URL, json=input_data)
            
            # 4. Handle the API's response
            if response.status_code == 200:
                # Parse the JSON response returned from app.py
                result = response.json()
                
                # Extract the value (using .get() safely handles the key name)
                prediction = result.get('Predicted_category', 'Unknown')
                
                # Display the successful result
                st.success(f"The predicted premium category is: **{prediction}**")
            else:
                # If FastAPI returns a 422 (validation error) or 500
                st.error(f"API Error ({response.status_code}): {response.text}")
                
        except requests.exceptions.ConnectionError:
            # Catch the error if the FastAPI server is offline
            st.error("Failed to connect to the API. Please ensure your FastAPI server is running.")