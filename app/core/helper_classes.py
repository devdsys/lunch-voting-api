import bcrypt
from sqlalchemy import Column, Integer, String, DateTime
from datetime import  datetime
from sqlalchemy.ext.declarative import declared_attr


class ModelFieldsBase:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AuthentificationBase(ModelFieldsBase):
    """Base class for authentication models"""
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def set_password(self, password: str):
        """Hash the password and store it as a string"""
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_pw.decode('utf-8') 

    def check_password(self, password: str):
        """Verify if the provided password matches the stored hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
