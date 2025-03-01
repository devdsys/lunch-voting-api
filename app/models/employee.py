# models/employee.py
from sqlalchemy import Column, Integer, String, Date
from datetime import date
from core.database import Base

class Employee(Base):
    """Employee model"""
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(Date, default=date.today)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', email='{self.email}')"