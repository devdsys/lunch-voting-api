import os
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
from jwt import encode
from fastapi.security import OAuth2PasswordBearer
from app.core.config import AUTH_PREFIX


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{AUTH_PREFIX}login")

def create_access_token(data: dict, expires_delta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=1))
    to_encode.update({"exp": expire})
    return encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=7))
    to_encode.update({"exp": expire})
    return encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
