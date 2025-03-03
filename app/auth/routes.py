from fastapi import APIRouter, Depends
from app.core.database import get_db, SessionLocal
from app.auth.schemas import Token, LoginRequest
from app.auth.services import login

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    return login(login_request, db)
