from pydantic import BaseModel
from typing import Optional
from enum import Enum
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError, encode, decode
from datetime import datetime, timedelta
from repositories.employee import EmployeeRepository
from models.employee import Employee
from fastapi import APIRouter
from core.database import get_db, SessionLocal

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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, "secret_key", algorithm="HS256")
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=7)  # refresh token expires in 7 days
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, "secret_key", algorithm="HS256")
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, "secret_key", algorithms=["HS256"])
        email: str = payload.get("email")
        role: str = payload.get("role")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email, role=role)
    except PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_data

def get_current_active_user(current_user: TokenData = Depends(get_current_user)):
    return current_user

class LoginRequest(BaseModel):
    email: str
    password: str
    role: Role

def login(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)  
    employee = employee_repository.get_employee_by_email(login_request.email)
    if not employee:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not employee.check_password(login_request.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"email": employee.email, "role": login_request.role}, expires_delta=access_token_expires
    )
    refresh_token_expires = timedelta(days=7)
    refresh_token = create_refresh_token(
        data={"email": employee.email, "role": login_request.role}, expires_delta=refresh_token_expires
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    login_request: LoginRequest,
    db: SessionLocal = Depends(get_db) 
):
    return login(login_request, db)