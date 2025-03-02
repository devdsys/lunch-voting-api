from fastapi import FastAPI
from auth.routes import router as auth_router
from routes.employee import router as employee_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(employee_router, prefix="/employee", tags=["Employee"])
