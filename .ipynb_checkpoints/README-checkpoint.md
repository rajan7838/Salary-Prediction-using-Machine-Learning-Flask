# Salary Prediction using Machine Learning & Flask

This project predicts employee salary based on demographic and job-related features
using machine learning regression models and deploys the best model using Flask.

---

## 🔹 Models Used
- KNN Regressor
- Decision Tree Regressor
- Random Forest Regressor

The best model is selected using **GridSearchCV** based on **R² score**.

---

## 🔹 Features
- Categorical variable handling using OneHotEncoder
- Feature scaling for distance-based models (KNN)
- Non-linear modeling using tree-based algorithms
- Hyperparameter tuning
- Data visualization using Matplotlib
- Flask-based web deployment

---

## 🔹 Dataset Features
- Education
- Experience
- Location
- Job Title
- Age
- Gender

**Target:** Salary


salary_prediction/
│
├── training.ipynb # Model training & visualization
├── app.py # Flask app
├── salary_model.pkl # Trained model
├── templates/
│ └── index.html
├── requirements.txt
└── README.md


## 🔹 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

Train the model:-python training.ipynb

Run Flask app:-python app.py