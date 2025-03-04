from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.routes.employee import router as employee_router
from app.routes.restaurant import router as restaurant_router
from app.routes.menu import router as menu_router
from app.routes.votes import router as votes_router
from app.core.config import (
    AUTH_PREFIX, 
    EMPLOYEE_PREFIX, 
    RESTAURANT_PREFIX,
    MENU_PREFIX,
    VOTES_PREFIX
)

app = FastAPI()

app.include_router(auth_router, prefix=f"{AUTH_PREFIX}", tags=["Auth"])
app.include_router(employee_router, prefix=f"{EMPLOYEE_PREFIX}", tags=["Employee"])
app.include_router(restaurant_router, prefix=f"{RESTAURANT_PREFIX}", tags=["Restaurant"])
app.include_router(votes_router, prefix=f"{VOTES_PREFIX}", tags=["Votes"])
app.include_router(menu_router, prefix=f"{MENU_PREFIX}", tags=["Menu"])