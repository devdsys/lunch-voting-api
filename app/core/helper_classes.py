import bcrypt
from sqlalchemy import Column, Integer, String, Date
from datetime import  datetime
from sqlalchemy.ext.declarative import declared_attr
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError
from app.validation.password_validation import PasswordValidator


class AuthentificationBase:
    """Base class for authentication models"""
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    created_at = Column(Date, default=datetime.utcnow)

    def set_password(self, password: str):
        """Hash the password and store it as a string"""
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_pw.decode('utf-8') 

    def check_password(self, password: str):
        """Verify if the provided password matches the stored hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
