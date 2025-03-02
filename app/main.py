from fastapi import FastAPI
from auth.routes import router as auth_router
from routes.employee import router as employee_router
from core.config import AUTH_PREFIX, EMPLOYEE_PREFIX

app = FastAPI()

app.include_router(auth_router, prefix=f"{AUTH_PREFIX}", tags=["Auth"])
app.include_router(employee_router, prefix=f"{EMPLOYEE_PREFIX}", tags=["Employee"])
