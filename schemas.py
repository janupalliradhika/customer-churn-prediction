from pydantic import BaseModel

class Customer(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract_One_year: int
    Contract_Two_year: int