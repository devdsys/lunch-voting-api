from pydantic import BaseModel, field_validator
from app.validation.registration_validators import CommonValidators
from datetime import datetime

class RestaurantBase(BaseModel):
    name: str
    address: str
    working_hours: str

class RestaurantCreate(RestaurantBase):
    email: str
    password: str

    @field_validator("email")
    def validate_email(cls, v):
        return CommonValidators.validate_email(v)

    @field_validator("password")
    def validate_password(cls, v):
        return CommonValidators.validate_password(v)

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