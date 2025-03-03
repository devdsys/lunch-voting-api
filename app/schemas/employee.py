from datetime import datetime
from pydantic import BaseModel, field_validator
from app.validation.registration_validators import CommonValidators


class EmployeeBase(BaseModel):
    """Base employee model"""
    name: str
    email: str

    @field_validator("email")
    def validate_email(cls, v):
        return CommonValidators.validate_email(v)

class EmployeeCreate(EmployeeBase):
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        return CommonValidators.validate_password(v)
    
class EmployeeUpdate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Employee(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True