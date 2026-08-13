# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning. It also includes a FastAPI application that validates customer input and provides prediction endpoints for both single and batch customer predictions. The project is built using the IBM Telco Customer Churn dataset.

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

```
IBM Telco Customer Churn Dataset
            │
            ▼
   Data Preprocessing
            │
            ▼
 Exploratory Data Analysis (EDA)
            │
            ▼
   Feature Engineering
            │
            ▼
     Model Training
            │
            ▼
    Model Evaluation
            │
            ▼
        FastAPI
            │
            ▼
 Customer Churn Prediction
```

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
├── api/
│   ├── app.py
│   ├── schemas.py
│   └── sample_data/
│       └── batch_customers.json
│
├── data/
├── docs/
├── models/
│   └── rf_model.pkl
├── notebooks/
│   └── eda.ipynb
├── sql/
├── Project_Screenshots/
├── README.md
├── error_report.md
└── .gitignore
```

---

## Dataset

**IBM Telco Customer Churn Dataset**

- Approximately 7,043 customer records
- 21 features
- Target Variable: **Churn**

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
- Exploratory Data Analysis (EDA)
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

### Day 19
- Implemented Batch Prediction API
- Created sample batch JSON file
- Added batch prediction endpoint

### Day 20
- Tested Batch Prediction API
- Performed API validation with multiple test cases
- Documented error handling
- Updated project documentation

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

## Single Customer Prediction

### Endpoint

```
POST /predict
```

### Valid Input

```json
{
  "tenure": 24,
  "MonthlyCharges": 75.5,
  "TotalCharges": 1800
}
```

### Expected Result

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

### Expected Result

FastAPI automatically returns validation errors.

---

# Batch Prediction API

## Endpoint

```
POST /batch_predict
```


## Purpose

Predict customer churn for multiple customers in a single API request.

---

## Input

The API accepts a JSON object containing multiple customer records.

Example:

```json
{
  "customers": [
    {
      "gender": 1,
      "SeniorCitizen": 0,
      "Partner": 1,
      "Dependents": 0,
      "tenure": 5,
      "PhoneService": 1,
      "PaperlessBilling": 1,
      "MonthlyCharges": 79.85,
      "TotalCharges": 399.25,
      "MultipleLines_No_phone_service": 0,
      "MultipleLines_Yes": 0,
      "InternetService_Fiber_optic": 1,
      "InternetService_No": 0,
      "OnlineSecurity_No_internet_service": 0,
      "OnlineSecurity_Yes": 0,
      "OnlineBackup_No_internet_service": 0,
      "OnlineBackup_Yes": 1,
      "DeviceProtection_No_internet_service": 0,
      "DeviceProtection_Yes": 1,
      "TechSupport_No_internet_service": 0,
      "TechSupport_Yes": 0,
      "StreamingTV_No_internet_service": 0,
      "StreamingTV_Yes": 1,
      "StreamingMovies_No_internet_service": 0,
      "StreamingMovies_Yes": 1,
      "Contract_One_year": 0,
      "Contract_Two_year": 0,
      "PaymentMethod_Credit_card_automatic": 0,
      "PaymentMethod_Electronic_check": 1,
      "PaymentMethod_Mailed_check": 0
    }
  ]
}
```

---

## Output

Example:

```json
{
  "predictions": [0]
}
```

### Prediction Labels

- **0** → Not Likely to Churn
- **1** → Likely to Churn

---

---

# Results

The project successfully predicts customer churn using machine learning models.

## Model Performance

- Logistic Regression
- Random Forest
- XGBoost

Random Forest provided the best prediction performance and was integrated with the FastAPI application.

## API Results

- Single customer prediction using `/predict`
- Batch prediction using `/batch_predict`
- Automatic request validation using Pydantic
- Interactive API documentation using Swagger UI

## Dashboard Results

The dashboard provides visual analysis of:

- Customer Churn Distribution
- Contract Type Distribution
- Monthly Charges Distribution
- Customer Tenure Distribution
- Internet Service Distribution

These visualizations help understand customer behavior and churn patterns.

---

## Features

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Customer Churn Prediction
- Customer Lifetime Value (LTV) Prediction
- Logistic Regression Model
- Random Forest Model
- XGBoost Model
- FastAPI REST API
- Single Customer Prediction
- Batch Customer Prediction
- Pydantic Input Validation
- Swagger API Documentation

---

## Testing

The API was tested with:

- Single customer prediction
- Batch prediction with 2 customers
- Batch prediction with 5 customers
- Batch prediction with 10 customers
- Invalid input validation
- Missing field validation
- Incorrect data type validation
- Empty customer list validation

---

## Future Improvement

# Future Scope

- Deploy the FastAPI application on a   cloud platform.
- Build a web application for customer churn prediction.
- Improve model accuracy through hyperparameter tuning.
- Add user authentication and authorization.
- Support CSV file upload for batch predictions.
- Integrate a real-time dashboard for business monitoring.

---

## License

This project is developed for educational and academic purposes.