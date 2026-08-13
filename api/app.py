from fastapi import FastAPI
from schemas import Customer, Customers
import joblib

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts customer churn risk and provides retention recommendations using a Random Forest model.",
    version="2.0"
)

# Load trained model
model = joblib.load("../models/rf_model.pkl")


# -----------------------------
# Helper Functions
# -----------------------------

def get_risk_level(churn_probability):
    """
    Categorize customer based on churn probability.
    """

    if churn_probability >= 0.70:
        return "HIGH"

    elif churn_probability >= 0.40:
        return "MEDIUM"

    else:
        return "LOW"


def get_risk_factors(customer):
    """
    Identify possible customer characteristics
    associated with higher churn risk.
    """

    risk_factors = []

    if customer.tenure <= 12:
        risk_factors.append("Short customer tenure")

    if customer.MonthlyCharges >= 70:
        risk_factors.append("High monthly charges")

    if (
        customer.Contract_One_year == 0
        and customer.Contract_Two_year == 0
    ):
        risk_factors.append("Month-to-month contract")

    if customer.PaymentMethod_Electronic_check == 1:
        risk_factors.append("Electronic check payment")

    if customer.PaperlessBilling == 1:
        risk_factors.append("Paperless billing")

    if not risk_factors:
        risk_factors.append("No major risk factors identified")

    return risk_factors


def get_recommendation(risk_level):
    """
    Generate retention recommendations based on risk level.
    """

    if risk_level == "HIGH":

        return [
            "Contact the customer immediately",
            "Offer a personalized discount",
            "Encourage long-term contract renewal"
        ]

    elif risk_level == "MEDIUM":

        return [
            "Send a customer engagement offer",
            "Provide loyalty benefits",
            "Encourage contract upgrade"
        ]

    else:

        return [
            "Continue regular customer engagement",
            "Provide loyalty rewards",
            "Monitor customer activity"
        ]


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API",
        "version": "2.0"
    }


# -----------------------------
# Single Customer Prediction
# -----------------------------

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

    try:

        # Get prediction
        prediction = model.predict(data)[0]

        # Get probability
        probabilities = model.predict_proba(data)[0]

        # Probability of class 1 = Churn
        churn_probability = float(probabilities[1])

        # Determine risk level
        risk_level = get_risk_level(churn_probability)

        # Identify possible risk factors
        risk_factors = get_risk_factors(customer)

        # Generate recommendations
        recommendations = get_recommendation(risk_level)

        # Convert prediction to readable text
        if prediction == 1:

            result = "Customer is Likely to Churn"

        else:

            result = "Customer is Not Likely to Churn"

        return {
            "Prediction": result,
            "Churn Probability": round(churn_probability * 100, 2),
            "Risk Level": risk_level,
            "Risk Factors": risk_factors,
            "Recommendations": recommendations
        }

    except Exception as e:

        return {
            "Error": str(e)
        }


# -----------------------------
# Batch Prediction
# -----------------------------

@app.post("/batch_predict")
def batch_predict(customers: Customers):

    all_data = []

    for customer in customers.customers:

        row = [
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
        ]

        all_data.append(row)

    try:

        # Get predictions
        predictions = model.predict(all_data)

        # Get probabilities
        probabilities = model.predict_proba(all_data)

        results = []

        for i, pred in enumerate(predictions):

            churn_probability = float(probabilities[i][1])

            risk_level = get_risk_level(churn_probability)

            if pred == 1:

                result = "Customer is Likely to Churn"

            else:

                result = "Customer is Not Likely to Churn"

            results.append({
                "Customer": i + 1,
                "Prediction": result,
                "Churn Probability": round(churn_probability * 100, 2),
                "Risk Level": risk_level
            })

        return {
            "Total Customers": len(results),
            "Results": results
        }

    except Exception as e:

        return {
            "Error": str(e)
        }