from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode
from app.auth.jwt import JWT_SECRET_KEY
from app.auth.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        token_data = TokenData(email=payload.get("email"), role=payload.get("role"))
        return token_data
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_employee(current_user: TokenData = Depends(get_current_user)):
    if current_user.role != "employee":
        raise HTTPException(status_code=403, detail="Forbidden")
    return current_user

def get_current_restaurant(current_user: TokenData = Depends(get_current_user)):
    if current_user.role != "restaurant":
        raise HTTPException(status_code=403, detail="Forbidden")
    return current_user