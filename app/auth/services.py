from datetime import timedelta
from fastapi import Depends, HTTPException
from app.core.database import get_db, SessionLocal
from app.auth.jwt import create_access_token, create_refresh_token
from app.auth.schemas import LoginRequest


def login(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    repository = login_request.role.repository
    if repository is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid role",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Validate the user's credentials
    user_repository = repository(db)
    user = user_repository.get_user_by_email(login_request.email)
    if not user or not user.check_password(login_request.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Create the JWT payload
    payload = {
        "email": user.email,
        "role": login_request.role
    }
    # Create the access token
    access_token = create_access_token(
        data=payload,
        expires_delta=timedelta(minutes=30),
    )
    # Create the refresh token
    refresh_token = create_refresh_token(
        data=payload,
        expires_delta=timedelta(days=7),
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}