import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('knn_model.pkl', 'rb'))

st.markdown("## 🛡️ Credit Card Fraud Detection")
st.markdown("Enter the values for each feature and click **Predict** to check if the transaction is fraudulent.")

input_values = []

with st.expander("🔍 Input Feature Values"):
    col1, col2 = st.columns(2)
    for i in range(30):  # 28 PCA features + Time & Amount
        with (col1 if i % 2 == 0 else col2):
            val = st.number_input(f"Feature V{i+1}", key=f"v{i+1}")
            input_values.append(val)

if st.button("Predict"):
    prediction = model.predict([input_values])
    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

st.markdown("---")
st.markdown("Made with ❤️ by [Ananya Arya](https://www.linkedin.com/in/ananya-arya-34a265257/)")
