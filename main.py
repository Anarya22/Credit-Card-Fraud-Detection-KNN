import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('knn_model.pkl', 'rb'))

st.markdown("## 🛡️ Credit Card Fraud Detection")
st.markdown("Enter the values for each feature and click **Predict** to check if the transaction is fraudulent.")

# Initialize session state for all input values
if 'initialized' not in st.session_state:
    for i in range(30):
        st.session_state[f"v{i + 1}"] = 0.0
    st.session_state.initialized = True

input_values = []

with st.expander("🔍 Input Feature Values"):
    col1, col2 = st.columns(2)
    for i in range(30):
        with (col1 if i % 2 == 0 else col2):
            val = st.number_input(
                f"Feature V{i + 1}",
                min_value=-100.0,
                max_value=100.0,
                value=st.session_state[f"v{i + 1}"],  # Use session state value
                step=0.1,
                key=f"v{i + 1}",
                help="Enter scaled feature value"
            )
            input_values.append(val)


def reset_values():
    """Callback function to reset all values to 0"""
    for i in range(30):
        st.session_state[f"v{i + 1}"] = 0.0


if st.button("Predict"):
    if all(val == 0.0 for val in input_values):
        st.warning("⚠️ Please enter valid (non-zero) feature values before predicting.")
    else:
        prediction = model.predict([input_values])
        if prediction[0] == 1:
            st.error("🚨 Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")

        # Add reset button that uses the callback
        st.button("🔁 Reset Values", on_click=reset_values)

st.markdown("---")
st.markdown("Made with ❤️")
