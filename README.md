# Customer Churn Prediction System

## Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning techniques. The system analyzes customer demographics, service usage, billing information, and contract details to identify customers who may leave the company.

The project includes:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- FastAPI Deployment
- Single Customer Prediction
- Batch Customer Prediction
- Dashboard Visualization

---

## Objective

The main objective of this project is to:

- Predict customer churn accurately.
- Help telecom companies identify customers at risk.
- Improve customer retention strategies.
- Provide predictions through a REST API.

---

## Dataset

Dataset Used:

**Telco Customer Churn Dataset**

Features include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn

---

## Project Structure

```text
customer-churn-prediction/

├── api/
│   ├── app.py
│   └── schemas.py
│
├── data/
│   ├── Telco-Customer-Churn.csv
│   ├── Telco-Customer-Churn-Clean.csv
│   └── dashboard_data.csv
│
├── docs/
│
├── models/
│   └── rf_model.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── Project_Screenshots/
│
├── sql/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Exploratory Data Analysis (EDA)

Performed:

- Missing Value Analysis
- Churn Distribution Analysis
- Contract Type Analysis
- Monthly Charges Analysis
- Tenure Analysis
- Correlation Heatmap
- Service Usage Analysis

---

## Feature Engineering

Created and processed features including:

- One-Hot Encoding
- Categorical Feature Transformation
- Service-Based Features
- Contract-Based Features
- Payment Method Features

Final model uses 30 features.

---

## Machine Learning Models Used

### 1. Logistic Regression

Purpose:

- Baseline model
- Easy interpretation
- Initial churn prediction

---

### 2. Random Forest Classifier

Purpose:

- Better accuracy
- Handles non-linear relationships
- Feature importance analysis

Final deployed model:

**Random Forest Classifier**

---

## Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Random Forest performed better than Logistic Regression and was selected for deployment.

---

## API Development

Framework Used:

**FastAPI**

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Customer Churn Prediction API"
}
```

---

### Single Prediction Endpoint

```http
POST /predict
```

Predicts churn for a single customer.

---

### Batch Prediction Endpoint

```http
POST /batch_predict
```

Predicts churn for multiple customers simultaneously.

---

## Running the API

### Step 1

Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2

Navigate to API folder

```bash
cd api
```

### Step 3

Start FastAPI Server

```bash
py -3.14 -m uvicorn app:app --reload
```

### Step 4

Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Dashboard

Dashboard includes:

- Customer Churn Distribution
- Contract Type Analysis
- Monthly Charges Analysis
- Internet Service Analysis
- Payment Method Analysis
- Correlation Analysis

---

## Batch Prediction Example

Input:

```json
{
  "customers": [
    {
      "gender": 1,
      "SeniorCitizen": 0,
      "Partner": 1,
      "Dependents": 0,
      "tenure": 24
    }
  ]
}
```

Output:

```json
{
  "Total Customers": 1,
  "Results": [
    {
      "Customer": 1,
      "Prediction": "Not Likely to Churn"
    }
  ]
}
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- FastAPI
- Uvicorn
- Git
- GitHub

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. API Development
8. Batch Prediction
9. Dashboard Visualization
10. Project Deployment Preparation

---

## Future Scope

- Deploy on Cloud Platforms
- Real-Time Customer Monitoring
- Integration with Telecom CRM Systems
- Advanced Dashboard using Metabase/Superset
- Automated Customer Retention Recommendations

---

## Team Members

- Radhika (Team Lead)
- Priya

---

## Conclusion

The Customer Churn Prediction System successfully predicts whether a customer is likely to churn using Machine Learning models. The project provides an easy-to-use FastAPI interface for both single and batch predictions and helps organizations take proactive customer retention measures.