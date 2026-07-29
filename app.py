from fastapi import FastAPI
from schemas import Customer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(customer: Customer):
    return {
        "status": "Success",
        "customer": customer.model_dump()   # If using Pydantic v2
    }