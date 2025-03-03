from app.repositories.employee import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def create_employee(self, employee: EmployeeCreate):
        return self.employee_repository.create_employee(employee)

    def get_employee(self, employee_id: int):
        return self.employee_repository.get_employee(employee_id)

    def update_employee(self, employee_id: int, employee: EmployeeUpdate):
        return self.employee_repository.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int):
        return self.employee_repository.delete_employee(employee_id)
    
    def get_employee_by_email(self, email: str):
        return self.employee_repository.get_user_by_email(email)