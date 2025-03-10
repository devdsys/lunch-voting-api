from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.core.database import SessionLocal


class EmployeeRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_employee(self, employee: EmployeeCreate):
        try:
            db_employee = Employee(name=employee.name, surname=employee.surname, email=employee.email)
            db_employee.set_password(employee.password)  
            self.db.add(db_employee)
            self.db.commit()
            self.db.refresh(db_employee)
            return db_employee
        except Exception as e:
            self.db.rollback() 
            raise e 

    def get_employee(self, employee_id: int):
        """Get an employee by ID from the database"""
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def update_employee(self, employee_id: int, employee: EmployeeUpdate):
        """Update an existing employee in the database"""
        db_employee = self.get_employee(employee_id)
        if db_employee:
            db_employee.name = employee.name
            self.db.commit()
            self.db.refresh(db_employee)
            return db_employee  # Return the updated Employee object
        return None

    def delete_employee(self, employee_id: int):
        """Delete an employee from the database"""
        db_employee = self.get_employee(employee_id)
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()
            return {"message": "Employee deleted successfully"}
        return None
    
    def get_user_by_email(self, email: str, ):
        return self.db.query(Employee).filter(Employee.email == email).first()