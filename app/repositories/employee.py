from models.employee import Employee
from schemas.employee import EmployeeCreate
from core.database import get_db, SessionLocal
from fastapi import Depends



class EmployeeRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_employee(self, employee: EmployeeCreate):
        try:
            db_employee = Employee(name=employee.name, email=employee.email)
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

    def update_employee(self, employee_id: int, employee: EmployeeCreate):
        """Update an existing employee in the database"""
        db_employee = self.get_employee(employee_id)
        if db_employee:
            db_employee.name = employee.name
            db_employee.email = employee.email
            self.db.commit()
            self.db.refresh(db_employee)
        return db_employee

    def delete_employee(self, employee_id: int):
        """Delete an employee from the database"""
        db_employee = self.get_employee(employee_id)
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()
        return db_employee
    
    def get_user_by_email(self, email: str, ):
        return self.db.query(Employee).filter(Employee.email == email).first()