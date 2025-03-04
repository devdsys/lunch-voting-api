from pydantic import BaseModel
from typing import Optional
from enum import Enum
from app.repositories.employee import EmployeeRepository
from app.repositories.restaurant import RestaurantRepository


class Role(str, Enum):
    employee = "employee"
    restaurant = "restaurant"

    @property
    def repository(self):
        repositories = {
            "employee": EmployeeRepository,
            "restaurant": RestaurantRepository,
        }
        return repositories[self.value]

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None
    id: Optional[int] = None

class LoginRequest(BaseModel):
    email: str
    password: str
    role: Role
