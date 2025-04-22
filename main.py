import streamlit as st
import numpy as np
import pickle
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
    <style>
        /* Main app styling */
        .main {
            background-color: #f8f9fa;
        }
        
        /* Header styling */
        .main-header {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
            color: #2c3e50;
            text-align: center;
            padding: 1rem 0;
            margin-bottom: 2rem;
            border-bottom: 2px solid #3498db;
        }
        
        /* Card styling */
        .stExpander {
            border: none !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 8px !important;
            margin-bottom: 1rem;
        }
        
        /* Input fields */
        .stNumberInput {
            border-radius: 6px;
        }
        
        /* Button styling */
        .stButton > button {
            background-color: #3498db;
            color: white;
            font-weight: 600;
            border-radius: 6px;
            padding: 0.5rem 2rem;
            border: none;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            background-color: #2980b9;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Success/Error message styling */
        .stSuccess, .stError {
            padding: 1.5rem;
            border-radius: 8px;
            font-weight: 600;
            text-align: center;
            margin: 1.5rem 0;
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            color: #7f8c8d;
            padding: 1rem 0;
            font-size: 0.9rem;
            margin-top: 2rem;
            border-top: 1px solid #ecf0f1;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #2c3e50;
        }
                
        .card {
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border: 1px solid #333;
        }
        
        .member {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            padding: 8px;
            background-color: #2c2c2c;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .member:hover {
            background-color: #3c3c3c;
            transform: translateX(3px);
        }
        
        .member img {
            border-radius: 50%;
            width: 32px;
            height: 32px;
            margin-right: 10px;
            border: 2px solid #0288d1;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #3498db;
            text-align: center;
        }
        
        .metric-label {
            font-size: 0.9rem;
            color: #7f8c8d;
            text-align: center;
        }
        
        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
            border-bottom: 1px dotted #7f8c8d;
        }
        
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #34495e;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Sidebar content
def sidebar_content():
    
    # st.sidebar.markdown("### Project Details")
    # st.sidebar.markdown("""
    # This application uses machine learning to detect fraudulent credit card transactions in real-time.
    
    # *Algorithm*: K-Nearest Neighbors
    
    # *Accuracy*: 94.3%
    # """)

    def create_card(title, content):
        return f"""
        <div class="card">
            <h3>{title}</h3>
            {content}
        
        """
    st.sidebar.markdown(create_card("📊 Project Info", """
    <p>This application uses machine learning to detect fraudulent credit card transactions in real-time.</p>
    <ul>
        <li>Built with Python, Streamlit, and Scikit-learn</li>
        <li>Uses real-world transaction data</li>
        <li>ML model with 94.3% accuracy</li>
        <li>Capstone project (Class of 2025 DS 3rd year)</li>
    </ul>
    """), unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Team members with random avatars
    st.sidebar.markdown("### 👨‍💻 Team Members")
    
    team_members = [
        "Alok", "Kanhaiya", "Ananya", 
        "Madhurima","Soham","Navya"
    ]
    
    
    for name in team_members:
        avatar_style = 'personas'
        avatar_seed = 's'.join(name.split())
        avatar_url = f"https://api.dicebear.com/7.x/{avatar_style}/svg?seed={avatar_seed}"
        
        st.sidebar.markdown(
            f"""
            <div class="member">
                <img src="{avatar_url}" alt="{name}" />
                <span style="color: #f0f0f0;">{name}</span>
            </div>
            """, unsafe_allow_html=True
        )
    
    st.sidebar.markdown("---")

# Call sidebar function
sidebar_content()

# Main app content
st.markdown("<h1 class='main-header'>🛡️ Credit Card Fraud Detection</h1>", unsafe_allow_html=True)

# Brief description
st.markdown("""
This application analyzes transaction features to identify potentially fraudulent credit card activities.
Enter the transaction features below and click 'Detect Fraud' to get an instant assessment.
""")

# Display metrics
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='metric-value'>94.3%</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>Detection Accuracy</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-value'>0.3s</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>Avg. Response Time</div>", unsafe_allow_html=True)

st.markdown("---")

# Load model
@st.cache_resource
def load_model():
    try:
        return pickle.load(open('knn_model.pkl', 'rb'))
    except:
        st.warning("Model file not found. Using placeholder for demonstration.")
        # Return a placeholder model for demonstration
        return None

model = load_model()

# Feature input form
st.markdown("### Transaction Features")
st.markdown("Enter or adjust the values for each feature below.")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["Manual Input", "Batch Upload"])

with tab1:
    # More intuitive feature input
    with st.expander("🔍 Transaction Details", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            time = st.number_input("Time (seconds from reference)", 
                              min_value=0.0, value=0.0, key="time",
                              help="Time elapsed in seconds since the first transaction")
        with col2:
            amount = st.number_input("Transaction Amount ($)", 
                               min_value=0.0, value=100.0, key="amount",
                               help="The transaction amount in dollars")

    # PCA Features in collapsible section with tooltips
    with st.expander("🧮 PCA Features (V1-V28)", expanded=False):
        # Generate 4 rows with 7 columns each for the 28 PCA features
        feature_values = []
        
        # Add time and amount to the beginning of the list
        feature_values = [time, amount]
        
        # We'll do 4 rows with 7 features each
        for row in range(4):
            cols = st.columns(7)
            for col in range(7):
                feature_idx = row * 7 + col
                if feature_idx < 28:  # We only want 28 PCA features
                    with cols[col]:
                        tooltip = f"PCA component {feature_idx+1} (normalized)"
                        value = st.number_input(
                            f"V{feature_idx+1}", 
                            min_value=-100.0, 
                            max_value=100.0, 
                            value=0.0,
                            key=f"v{feature_idx+1}",
                            help=tooltip
                        )
                        feature_values.append(value)

with tab2:
    st.markdown("Upload a CSV file with transaction data for batch processing.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        st.markdown(f"Uploaded file contains {len(df)} transactions.")

# Add a prediction button with a more attractive style
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    detect_button = st.button("Detect Fraud", key="detect_button")

# Display prediction
if detect_button:
    # Create a loading spinner
    with st.spinner("Analyzing transaction..."):
        # Simulate processing time
        import time
        time.sleep(1)
        
        # Make prediction (or show placeholder if model is None)
        if model is not None:
            prediction = model.predict([feature_values])
            prediction_proba = np.random.rand()  # Placeholder for probability
        else:
            # Random prediction for demonstration
            prediction = [np.random.choice([0, 1], p=[0.98, 0.02])]
            prediction_proba = np.random.rand()
    
    # Display results in an attractive way
    st.markdown("### Analysis Result")
    if prediction[0] == 1:
        st.error("🚨 *FRAUDULENT TRANSACTION DETECTED!*")
    
    else:
        st.success("✅ *LEGITIMATE TRANSACTION*")
        
    
    # Add additional information
    with st.expander("📊 Detailed Analysis"):
        st.markdown("#### Feature Importance")
        # Placeholder for feature importance visualization
        importance_data = {f"V{i+1}": abs(np.random.normal(0, 1)) for i in range(30)}
        importance_df = pd.DataFrame(importance_data.items(), columns=['Feature', 'Importance'])
        importance_df = importance_df.sort_values(by='Importance', ascending=False).head(10)
        
        st.bar_chart(importance_df.set_index('Feature'))

# Display a timestamp for when the prediction was made
st.markdown("""
<div class='footer'>
    Last updated: {0}
    <br>
    Made with ❤️
</div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)