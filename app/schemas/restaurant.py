from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError
from app.validation.password_validation import PasswordValidator
from datetime import datetime

class RestaurantBase(BaseModel):
    name: str
    address: str
    working_hours: str

class RestaurantCreate(RestaurantBase):
    email: str
    password: str

    @staticmethod
    def validate_email(email: str):
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return email

    @staticmethod
    def validate_password(password: str):
        password_validator = PasswordValidator(password)
        if not password_validator.is_valid():
            error_message = password_validator.get_error_message()
            raise ValueError(error_message)
        return password

class RestaurantUpdate(BaseModel):
    name: str
    address: str
    working_hours: str

class Restaurant(RestaurantBase):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True