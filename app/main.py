from fastapi import FastAPI, Depends
from services.employee import EmployeeService
from repositories.employee import EmployeeRepository
from core.database import SessionLocal
from schemas.employee import EmployeeCreate, Employee
from typing import List

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create employee endpoint
@app.post("/employees/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db = Depends(get_db)):
    """Create a new employee"""
    employee_service = EmployeeService(EmployeeRepository(db))
    return employee_service.create_employee(employee)

# Get all employees endpoint
@app.get("/employees/", response_model=List[Employee])
def get_employees(db = Depends(get_db)):
    """Get all employees"""
    employee_service = EmployeeService(EmployeeRepository(db))
    employees = db.query(Employee).all()
    return employees

# Get employee by ID endpoint
@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db = Depends(get_db)):
    """Get an employee by ID"""
    employee_service = EmployeeService(EmployeeRepository(db))
    return employee_service.get_employee(employee_id)

# Update employee endpoint
@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate, db = Depends(get_db)):
    """Update an existing employee"""
    employee_service = EmployeeService(EmployeeRepository(db))
    return employee_service.update_employee(employee_id, employee)

# Delete employee endpoint
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db = Depends(get_db)):
    """Delete an employee"""
    employee_service = EmployeeService(EmployeeRepository(db))
    return employee_service.delete_employee(employee_id)