from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, Enum, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.helper_classes import ModelFieldsBase
from enum import Enum as PyEnum

class DayOfWeek(PyEnum):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

class Menu(ModelFieldsBase, Base):
    """Menu model"""
    __tablename__ = "menu"
    name = Column(String)
    description = Column(String)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    day = Column(Enum(DayOfWeek, name="day_of_week_enum", create_type=False), nullable=False) 
    restaurant = relationship("Restaurant", backref="menus")

    __table_args__ = (
        UniqueConstraint("restaurant_id", "day", name="unique_menu_per_day"),
    )

    def __repr__(self):
        return f"Menu(id={self.id}, description='{self.description}', restaurant_id={self.restaurant_id}, day={self.day.value})"
