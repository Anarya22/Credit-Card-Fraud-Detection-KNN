# 🛡️ Credit Card Fraud Detection using K-Nearest Neighbors (KNN)

This project aims to detect fraudulent credit card transactions using the K-Nearest Neighbors (KNN) algorithm. The dataset used is highly imbalanced, with fraudulent transactions making up only a small fraction of the total. This project includes preprocessing, model training, evaluation, and optional deployment as a web app.

---

## 📊 Dataset

- **Source:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Note:** The dataset contains 284,807 transactions with 31 features, including the target class.
- **Disclaimer:** Due to GitHub's 25MB file limit, the dataset is not uploaded directly here. Please download it manually from the link above.

---

## 📁 Project Structure

credit-card-fraud-detection-knn/
│
├── data/                          # 💾 Data folder (dataset to be downloaded manually from Kaggle)
│   └── creditcard.csv            # (not included in repo due to size limits)
│
├── notebooks/                     # 📓 Jupyter Notebooks
│   └── Credit Card Fraud Detection.ipynb     # Main analysis and modeling notebook
│
├── models/                        # 🤖 Trained and serialized ML models
│   └── knn_model.pkl             # Pickle file for the trained KNN model
│
├── app/                           # 🌐 Web app files
│   └── main.py          # Streamlit app for real-time predictions
│
├── outputs/                       # 📊 Outputs and plots
│   ├── confusion_matrix.jpg      # Evaluation visualizations
│   └── classification_report # Detailed metrics
│
├── requirements.txt               # 📦 Python dependencies
├── README.md                      # 📘 Project documentation
├── .gitignore                     # 🚫 Files to ignore in version control



## 🔍 Features & Techniques

- 📌 **Data Preprocessing**  
  - Standardization of `Amount` and `Time`
  - Handling missing values and feature scaling

- 🧠 **Model**  
  - K-Nearest Neighbors Classifier

- ⚖️ **Imbalance Handling**  
  - Under-sampling of the majority class to improve fraud detection

- 📈 **Evaluation**  
  - Confusion Matrix  
  - Classification Report (Precision, Recall, F1-Score)  
  - ROC-AUC Score

- 🖥️ **Deployment**  
  - Streamlit app for real-time predictions

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://https://github.com/Anarya22/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
```
2. Install dependencies(Optional as it is already in this repository): pip install -r requirements.txt
3. Download the dataset from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
4. Run the Jupyter Notebook: Credit Card Fraud Detection.ipynb
5. Run the Streamlit app: streamlit run main.py
