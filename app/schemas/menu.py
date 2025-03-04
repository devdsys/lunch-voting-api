from pydantic import BaseModel
from app.models.menu import DayOfWeek

class MenuBase(BaseModel):
    name: str
    description: str
    day: DayOfWeek
    restaurant_id: int

class MenuCreate(MenuBase):
    pass

class MenuUpdate(MenuBase):
    pass

class Menu(MenuBase):
    id: int
    
    class Config:
        orm_mode = True