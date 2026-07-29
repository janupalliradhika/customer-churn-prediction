from fastapi import FastAPI
from schemas import Customer
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../models/rf_model.pkl")

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(customer: Customer):

    data = [[
        customer.gender,
        customer.SeniorCitizen,
        customer.Partner,
        customer.Dependents,
        customer.tenure,
        customer.PhoneService,
        customer.PaperlessBilling,
        customer.MonthlyCharges,
        customer.TotalCharges,
        customer.MultipleLines_No_phone_service,
        customer.MultipleLines_Yes,
        customer.InternetService_Fiber_optic,
        customer.InternetService_No,
        customer.OnlineSecurity_No_internet_service,
        customer.OnlineSecurity_Yes,
        customer.OnlineBackup_No_internet_service,
        customer.OnlineBackup_Yes,
        customer.DeviceProtection_No_internet_service,
        customer.DeviceProtection_Yes,
        customer.TechSupport_No_internet_service,
        customer.TechSupport_Yes,
        customer.StreamingTV_No_internet_service,
        customer.StreamingTV_Yes,
        customer.StreamingMovies_No_internet_service,
        customer.StreamingMovies_Yes,
        customer.Contract_One_year,
        customer.Contract_Two_year,
        customer.PaymentMethod_Credit_card_automatic,
        customer.PaymentMethod_Electronic_check,
        customer.PaymentMethod_Mailed_check
    ]]

    prediction = model.predict(data)

    return {
        "Prediction": int(prediction[0])
    }
