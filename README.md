# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning. It also includes a FastAPI application that validates customer input and provides a prediction endpoint. The project is built using the IBM Telco Customer Churn dataset.

---

## Aim

To predict whether a telecom customer is likely to churn using machine learning models and provide predictions through a FastAPI application.

---

## Team Members

- Janupalli Radhika
- Nithish Vanam
- Priya
- Prasanta
- Anish

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- PostgreSQL
- SQL
- FastAPI
- Pydantic
- Git
- GitHub

---

## Project Workflow

Dataset

↓

Data Preprocessing

↓

Exploratory Data Analysis (EDA)

↓

Feature Engineering

↓

Model Training

↓

Model Evaluation

↓

FastAPI

↓

Customer Churn Prediction

---

## Models Used

- Logistic Regression
- Random Forest
- XGBoost

---

## Project Structure

```
customer-churn-prediction/
│
├── data/
├── docs/
├── notebooks/
├── sql/
├── app.py
├── schemas.py
├── README.md
└── venv/
```

---

## Dataset

IBM Telco Customer Churn Dataset

- Approximately 7,043 customer records
- 21 features
- Target Variable: Churn

---

## Progress Summary

### Day 1
- Created GitHub repository
- Created project folder structure
- Uploaded IBM Telco Customer Churn dataset

### Day 2
- Installed PostgreSQL
- Created database
- Imported dataset
- Verified SQL queries

### Day 3–10
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering

### Day 11
- Logistic Regression Model

### Day 12–13
- Random Forest Model Training

### Day 14
- SHAP Explainability Analysis

### Day 15
- Customer Lifetime Value (LTV) Regression Model

### Day 16
- XGBoost Cross Validation

### Day 17
- Customer Input Schema using Pydantic

### Day 18
- API Input Validation using FastAPI
- Customer request validation
- Automatic validation errors

---

# API Usage

## Run FastAPI

```bash
python -m uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## Open Swagger UI

Open:

```
http://127.0.0.1:8000/docs
```

---

## Test Prediction

### Valid Input

```json
{
  "tenure": 24,
  "MonthlyCharges": 75.5,
  "TotalCharges": 1800
}
```

Expected Result

```
Status: Success
```

---

### Invalid Input

```json
{
  "tenure": -5,
  "MonthlyCharges": -30,
  "TotalCharges": -200
}
```

Expected Result

FastAPI automatically returns validation errors.

---

## Features

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Churn Prediction
- Cross Validation
- Customer Lifetime Value Prediction
- FastAPI REST API
- Pydantic Input Validation

---

## Future Improvements

- Integrate trained Random Forest model with FastAPI
- Deploy API to cloud
- Build web interface
- Add authentication
- Improve model performance
