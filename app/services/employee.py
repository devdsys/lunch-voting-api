from repositories.employee import EmployeeRepository
from schemas.employee import EmployeeCreate

class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def create_employee(self, employee: EmployeeCreate):
        """Create a new employee"""
        return self.employee_repository.create_employee(employee)

    def get_employee(self, employee_id: int):
        """Get an employee by ID"""
        return self.employee_repository.get_employee(employee_id)

    def update_employee(self, employee_id: int, employee: EmployeeCreate):
        """Update an existing employee"""
        return self.employee_repository.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int):
        """Delete an employee"""
        return self.employee_repository.delete_employee(employee_id)
    
    def get_employee_by_email(self, email: str):
        return self.employee_repository.get_user_by_email(email)