from pydantic import BaseModel, field_validator
from datetime import datetime
from validation.password_validation import PasswordValidator

class EmployeeBase(BaseModel):
    """Base employee model"""
    name: str
    email: str

class EmployeeCreate(EmployeeBase):
    """Employee creation model"""
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        password_validator = PasswordValidator(v)
        if not password_validator.is_valid():
            error_message = password_validator.get_error_message()
            raise ValueError(error_message)
        return v

class Employee(EmployeeBase):
    """Employee model with ID"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True