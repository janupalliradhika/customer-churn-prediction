# Customer Churn Prediction Using Machine Learning and FastAPI

## Project Report

---

# 1. Project Title

**Customer Churn Prediction Using Machine Learning and FastAPI**

---

# 2. Objective

The objective of this project is to predict whether a telecom customer is likely to discontinue (churn) the telecom service using machine learning techniques. The project also provides a FastAPI-based REST API that allows users to predict churn for both single and multiple customers. Additionally, an interactive dashboard is created to visualize customer behavior and business insights.

---

# 3. Dataset

The project uses the **IBM Telco Customer Churn Dataset**.

### Dataset Information

- Dataset Name: IBM Telco Customer Churn
- Total Records: 7,043
- Features: 21
- Target Variable: Churn

### Important Features

- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges
- Churn

---

# 4. Data Cleaning

Several preprocessing steps were performed before model training.

### Data Cleaning Steps

- Removed unnecessary columns
- Checked missing values
- Converted TotalCharges to numeric datatype
- Removed blank records
- Verified duplicate records
- Converted categorical variables into machine-readable format
- Standardized dataset for model training

The cleaned dataset was then used for exploratory data analysis and machine learning.

---

# 5. Exploratory Data Analysis (EDA)

EDA was performed to understand customer behavior and identify important patterns affecting churn.

### Visualizations Created

- Customer Churn Distribution
- Contract Type Distribution
- Monthly Charges Distribution
- Customer Tenure Distribution
- Internet Service Distribution
- Correlation Heatmap

### Key Observations

- Customers with month-to-month contracts showed higher churn.
- Customers with Fiber Optic internet service had higher churn rates.
- Customers with shorter tenure were more likely to churn.
- Higher monthly charges were associated with increased churn.

---

# 6. Feature Engineering

Feature engineering improved the quality of input data for machine learning models.

### Steps Performed

- Label Encoding
- One-Hot Encoding
- Handling categorical variables
- Feature selection
- Data transformation
- Train-Test Split

The processed dataset was then used for model development.

---

# 7. Model Training

Three machine learning models were developed and compared.

## Logistic Regression

- Simple linear classification model
- Used as the baseline model

## Random Forest

- Ensemble learning algorithm
- Multiple decision trees
- Better accuracy and robustness
- Selected as the final deployed model

## XGBoost

- Gradient Boosting algorithm
- High predictive performance
- Used for comparison

---

# 8. Model Evaluation

Models were evaluated using multiple performance metrics.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Cross Validation

Among all models, **Random Forest** achieved the best overall performance and was integrated into the API.

---

# 9. FastAPI Implementation

A REST API was developed using FastAPI to serve the trained machine learning model.

## Features

- Automatic API documentation
- Request validation using Pydantic
- Single customer prediction
- Batch customer prediction
- Interactive Swagger UI

### API Endpoints

#### GET /

Returns a welcome message.

#### POST /predict

Predicts churn for a single customer.

Input:

One customer record

Output:

Prediction result

#### POST /batch_predict

Predicts churn for multiple customers simultaneously.

Input:

JSON containing multiple customer records.

Output:

Prediction for every customer.

---

# 10. Dashboard

A dashboard was prepared to visualize important customer insights.

### Dashboard Charts

- Customer Churn Distribution
- Contract Type Distribution
- Monthly Charges Distribution
- Customer Tenure Distribution
- Internet Service Distribution

### Benefits

The dashboard helps users:

- Understand customer behavior
- Analyze churn patterns
- Compare customer categories
- Support business decision-making

---

# 11. Results

The project successfully predicts telecom customer churn using machine learning.

### Achievements

- Data cleaned successfully
- EDA completed
- Feature engineering performed
- Three machine learning models trained
- Random Forest selected as the final model
- FastAPI developed successfully
- Batch prediction implemented
- Dashboard created
- API tested using Swagger UI

---

# 12. Technologies Used

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
- Power BI

---

# 13. Future Scope

The project can be enhanced by:

- Deploying the API to cloud platforms such as Azure, AWS, or Render
- Building a web application for customer prediction
- Supporting CSV file upload for bulk predictions
- Integrating real-time dashboards
- Improving model accuracy through hyperparameter tuning
- Adding user authentication and authorization

---

# 14. Conclusion

The Customer Churn Prediction project demonstrates how machine learning can help telecom companies identify customers who are likely to leave their services.

The project covers the complete machine learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, API development, batch prediction, and dashboard visualization.

Random Forest produced the best prediction performance and was integrated with FastAPI to provide real-time predictions. The dashboard offers valuable business insights that help organizations make informed decisions for customer retention.

Overall, this project provides a practical and scalable solution for telecom customer churn prediction.

---

# Team Members

- Janupalli Radhika
- Priya
- Nithish Vanam
- Prasanta
- Anish

---

# GitHub Repository

Customer Churn Prediction Project

---

# Thank You
