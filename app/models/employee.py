from sqlalchemy import Column, String
from app.core.helper_classes import AuthentificationBase
from app.core.database import Base


class Employee(AuthentificationBase, Base):
    """Employee model"""
    surname = Column(String)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', email='{self.email}')"