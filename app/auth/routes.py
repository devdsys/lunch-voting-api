from fastapi import APIRouter, Depends
from core.database import get_db, SessionLocal
from auth.schemas import Token, LoginRequest
from auth.services import login

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    return login(login_request, db)
