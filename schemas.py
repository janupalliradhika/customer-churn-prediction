from pydantic import BaseModel, Field
from typing import List

class Customer(BaseModel):
    tenure: int = Field(..., ge=0)
    MonthlyCharges: float = Field(..., gt=0)
    TotalCharges: float = Field(..., ge=0)

    Contract_One_year: int = Field(0, ge=0, le=1)
    Contract_Two_year: int = Field(0, ge=0, le=1)


class BatchCustomers(BaseModel):
    customers: List[Customer]