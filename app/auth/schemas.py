from pydantic import BaseModel
from typing import Optional
from enum import Enum
from repositories.employee import EmployeeRepository


class Role(str, Enum):
    employee = "employee"

    @property
    def repository(self):
        repositories = {
            "employee": EmployeeRepository,
        }
        return repositories[self.value]

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
