# Day 25 - API Integration and Testing

## Objective

Test and verify the Customer Churn Prediction API developed using FastAPI.

## API Endpoints Tested

### 1. Home Endpoint

**Method:** GET

**Endpoint:**
`/`

Purpose:
- Verify that the FastAPI application is running successfully.

---

### 2. Single Customer Prediction

**Method:** POST

**Endpoint:**
`/predict`

Purpose:
- Accept a single customer record.
- Pass the customer data to the trained Random Forest model.
- Return whether the customer is likely to churn.

---

### 3. Batch Customer Prediction

**Method:** POST

**Endpoint:**
`/batch_predict`

Purpose:
- Accept multiple customer records together.
- Generate predictions for all customers.
- Return the prediction for each customer.

## Testing Process

1. Started the FastAPI application using Uvicorn.
2. Opened the Swagger API documentation.
3. Tested the home endpoint.
4. Tested single customer prediction.
5. Tested batch prediction using multiple customer records.
6. Verified that the Random Forest model successfully generated predictions.
7. Checked the API responses for errors.

## Result

The Customer Churn Prediction API was successfully tested for single and batch customer prediction.

## Technology Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Random Forest Classifier
- Joblib