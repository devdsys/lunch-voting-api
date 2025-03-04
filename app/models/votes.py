from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, CheckConstraint, Date
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.helper_classes import ModelFieldsBase
from datetime import date

class Votes(ModelFieldsBase, Base):
    """Votes model"""
    __tablename__ = "votes"
    menu_id = Column(Integer, ForeignKey("menu.id"))
    menu = relationship("Menu", backref="votes")
    employee_id = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Employee", backref="votes")
    stars = Column(Integer, nullable=False)
    date = Column(Date, default=date.today, nullable=False) 

    __table_args__ = (
        UniqueConstraint("menu_id", "employee_id", "date", name="unique_vote_per_menu_per_day"),
        CheckConstraint("stars BETWEEN 1 AND 5", name="valid_stars"),
    )

    def __repr__(self):
        return (f"Votes(id={self.id}, menu_id={self.menu_id}, employee_id={self.employee_id}, "
                f"stars={self.stars}, date={self.date}, created_at={self.created_at})")