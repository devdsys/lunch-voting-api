from datetime import timedelta
from fastapi import Depends, HTTPException
from core.database import get_db, SessionLocal
from repositories.employee import EmployeeRepository
from auth.jwt import create_access_token, create_refresh_token
from auth.schemas import LoginRequest

def login(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    employee = employee_repository.get_employee_by_email(login_request.email)

    if not employee or not employee.check_password(login_request.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"email": employee.email, "role": login_request.role},
        expires_delta=timedelta(minutes=30),
    )
    refresh_token = create_refresh_token(
        data={"email": employee.email, "role": login_request.role},
        expires_delta=timedelta(days=7),
    )

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
