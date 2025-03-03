from sqlalchemy import Column, String
from app.core.helper_classes import AuthentificationBase
from app.core.database import Base

class Restaurant(AuthentificationBase, Base):
    """Restaurant model"""
    address = Column(String)
    working_hours = Column(String)
    
    def __init__(self, name, address, working_hours, email, password):
        self.name = name
        self.address = address
        self.working_hours = working_hours
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f"Restaurant(id={self.id}, name='{self.name}', address='{self.address}', working_hours='{self.working_hours}')"