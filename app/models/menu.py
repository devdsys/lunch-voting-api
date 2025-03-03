from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Integer, Date
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.helper_classes import ModelFieldsBase
from enum import Enum 
from sqlalchemy import Enum as SQLAlchemyEnum

class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class Menu(ModelFieldsBase, Base):
    """Menu model"""
    __tablename__ = "menu"
    description = Column(String)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    day = Column(SQLAlchemyEnum(DayOfWeek))
    restaurant = relationship("Restaurant", backref="menus")

    __table_args__ = (
        UniqueConstraint("restaurant_id", "day", name="unique_menu_per_day"),
    )

    def __repr__(self):
        return f"Menu(id={self.id}, name='{self.name}', restaurant_id={self.restaurant_id}, day={self.day})"