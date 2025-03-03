from fastapi import APIRouter, Depends, HTTPException
from services.employee import EmployeeService
from repositories.employee import EmployeeRepository
from core.database import get_db
from schemas.employee import EmployeeCreate, Employee, EmployeeUpdate
from core.dependencies import get_current_employee
from auth.schemas import TokenData

router = APIRouter()

class EmployeeController:
    def __init__(self, db=Depends(get_db)):
        self.employee_service = EmployeeService(EmployeeRepository(db))

    def get_employee_or_404(self, employee_id: int, current_user: TokenData):
        db_employee = self.employee_service.get_employee(employee_id)
        if db_employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        if db_employee.email != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")
        return db_employee

    def create_employee(self, employee: EmployeeCreate):
        existing_employee = self.employee_service.get_employee_by_email(employee.email)
        if existing_employee:
            raise HTTPException(status_code=400, detail="Employee with this email already exists")
        return self.employee_service.create_employee(employee)

    def get_employee(self, employee_id: int, current_user: TokenData):
        return self.get_employee_or_404(employee_id, current_user)

    def update_employee(self, employee_id: int, employee: EmployeeUpdate, current_user: TokenData):
        self.get_employee_or_404(employee_id, current_user)
        return self.employee_service.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int, current_user: TokenData):
        self.get_employee_or_404(employee_id, current_user)
        return self.employee_service.delete_employee(employee_id)
    

def get_controller(db=Depends(get_db)):
    return EmployeeController(db)

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, controller: EmployeeController = Depends(get_controller)):
    return controller.create_employee(employee)

@router.get("/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, current_user: TokenData = Depends(get_current_employee), controller: EmployeeController = Depends(get_controller)):
    return controller.get_employee(employee_id, current_user)

@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate, current_user: TokenData = Depends(get_current_employee), controller: EmployeeController = Depends(get_controller)):
    return controller.update_employee(employee_id, employee, current_user)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, current_user: TokenData = Depends(get_current_employee), controller: EmployeeController = Depends(get_controller)):
    return controller.delete_employee(employee_id, current_user)