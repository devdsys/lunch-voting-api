from datetime import datetime
from pydantic import BaseModel, field_validator
from validation.password_validation import PasswordValidator
from email_validator import validate_email, EmailNotValidError


class EmployeeBase(BaseModel):
    """Base employee model"""
    name: str
    email: str

    @field_validator("email")
    def validate_email(cls, v):
        try:
            validate_email(v)
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return v

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