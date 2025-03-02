from fastapi import APIRouter, Depends, HTTPException
from services.employee import EmployeeService
from repositories.employee import EmployeeRepository
from core.database import get_db
from schemas.employee import EmployeeCreate, Employee


router = APIRouter()

class EmployeeController:
    def __init__(self, db=Depends(get_db)):
        self.employee_service = EmployeeService(EmployeeRepository(db))

    def create_employee(self, employee: EmployeeCreate):
        existing_employee = self.employee_service.get_employee_by_email(employee.email)
        if existing_employee:
            raise HTTPException(status_code=400, detail="Employee with this email already exists")
        return self.employee_service.create_employee(employee)

    def get_employee(self, employee_id: int):
        employee = self.employee_service.get_employee(employee_id)
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def update_employee(self, employee_id: int, employee: EmployeeCreate):
        return self.employee_service.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int):
        return self.employee_service.delete_employee(employee_id)

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db=Depends(get_db)):
    controller = EmployeeController(db)
    return controller.create_employee(employee)

@router.get("/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db=Depends(get_db)):
    controller = EmployeeController(db)
    return controller.get_employee(employee_id)

@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate, db=Depends(get_db)):
    controller = EmployeeController(db)
    return controller.update_employee(employee_id, employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db=Depends(get_db)):
    controller = EmployeeController(db)
    return controller.delete_employee(employee_id)
