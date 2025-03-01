from sqlalchemy import Column, Integer, String, Date
from datetime import date
from core.database import Base
import bcrypt


class Employee(Base):
    """Employee model"""
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)  # Stores hashed password as a string
    created_at = Column(Date, default=date.today)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def set_password(self, password: str):
        """Hash the password and store it as a string"""
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_pw.decode('utf-8') 

    def check_password(self, password: str):
        """Verify if the provided password matches the stored hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', email='{self.email}')"