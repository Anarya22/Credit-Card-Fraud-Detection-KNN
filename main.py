# streamlit_app.py
import streamlit as st
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load trained model
model = pickle.load(open('knn_model.pkl', 'rb'))

st.title("Credit Card Fraud Detector")
input_values = []

for i in range(30):  # Assuming 28 features after PCA
    val = st.number_input(f"Feature V{i+1}")
    input_values.append(val)

if st.button("Predict"):
    prediction = model.predict([input_values])
    st.write("Fraudulent" if prediction[0] == 1 else "Legitimate")
