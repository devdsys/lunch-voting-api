from app.models.menu import Menu
from app.core.database import SessionLocal
from app.schemas.menu import MenuCreate, MenuUpdate
from app.models.menu import DayOfWeek

class MenuRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_menu(self, restaurant_id: int, day: DayOfWeek, menu: MenuCreate):
        try:
            db_menu = Menu(name=menu.name, description=menu.description, restaurant_id=restaurant_id, day=day)
            self.db.add(db_menu)
            self.db.commit()
            self.db.refresh(db_menu)
            return db_menu
        except Exception as e:
            self.db.rollback()
            raise e

    def get_menu(self, restaurant_id: int, day: DayOfWeek):
        return self.db.query(Menu).filter(Menu.restaurant_id == restaurant_id, Menu.day == day).first()

    def update_menu(self, restaurant_id: int, day: DayOfWeek, menu: MenuUpdate):
        db_menu = self.get_menu(restaurant_id, day)
        if db_menu:
            db_menu.description = menu.description
            self.db.commit()
            self.db.refresh(db_menu)
            return db_menu
        return None

    def delete_menu(self, restaurant_id: int, day: DayOfWeek):
        db_menu = self.get_menu(restaurant_id, day)
        if db_menu:
            self.db.delete(db_menu)
            self.db.commit()
            return {"message": "Menu deleted successfully"}
        return None