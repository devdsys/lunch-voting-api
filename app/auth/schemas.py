from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Role(str, Enum):
    employee = "employee"
    restaurant = "restaurant"

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str
    role: Role
