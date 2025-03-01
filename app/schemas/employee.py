from pydantic import BaseModel, validator
from datetime import datetime

class EmployeeBase(BaseModel):
    """Base employee model"""
    name: str
    email: str

class EmployeeCreate(EmployeeBase):
    """Employee creation model"""
    password: str

class Employee(EmployeeBase):
    """Employee model with ID"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True