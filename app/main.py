from fastapi import FastAPI, Depends, HTTPException
from services.employee import EmployeeService
from repositories.employee import EmployeeRepository
from core.database import get_db
from schemas.employee import EmployeeCreate, Employee
from auth.jwt import router


app = FastAPI()
app.include_router(router)

class EmployeeController:
    def __init__(self, db = Depends(get_db)):
        self.employee_service = EmployeeService(EmployeeRepository(db))

    def create_employee(self, employee: EmployeeCreate):
        """Create a new employee"""
        existing_employee = self.employee_service.get_employee_by_email(employee.email)
        if existing_employee:
            raise HTTPException(status_code=400, detail="Employee with this email already exists")
        return self.employee_service.create_employee(employee)

    def get_employee(self, employee_id: int):
        """Get an employee by ID"""
        employee = self.employee_service.get_employee(employee_id)
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def update_employee(self, employee_id: int, employee: EmployeeCreate):
        """Update an existing employee"""
        return self.employee_service.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int):
        """Delete an employee"""
        return self.employee_service.delete_employee(employee_id)


@app.post("/employee/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db = Depends(get_db)):
    """Create a new employee"""
    controller = EmployeeController(db)
    return controller.create_employee(employee)

@app.get("/employee/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db = Depends(get_db)):
    """Get an employee by ID"""
    controller = EmployeeController(db)
    return controller.get_employee(employee_id)

@app.put("/employee/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate, db = Depends(get_db)):
    """Update an existing employee"""
    controller = EmployeeController(db)
    return controller.update_employee(employee_id, employee)

@app.delete("/employee/{employee_id}")
def delete_employee(employee_id: int, db = Depends(get_db)):
    """Delete an employee"""
    controller = EmployeeController(db)
    return controller.delete_employee(employee_id)
