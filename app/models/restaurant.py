from sqlalchemy import Column, Integer, String, Date
from datetime import date
from app.core.database import Base
import bcrypt 

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    working_hours = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(Date, default=date.today)

    def __init__(self, name, address, working_hours, email, password):
        self.name = name
        self.address = address
        self.working_hours = working_hours
        self.email = email
        self.set_password(password)

    def set_password(self, password: str):
        """Hash the password and store it as a string"""
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_pw.decode('utf-8') 

    def check_password(self, password: str):
        """Verify if the provided password matches the stored hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"Restaurant(id={self.id}, name='{self.name}', address='{self.address}', working_hours='{self.working_hours}')"