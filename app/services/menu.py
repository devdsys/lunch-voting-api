from app.repositories.menu import MenuRepository
from app.schemas.menu import MenuCreate, MenuUpdate
from app.models.menu import DayOfWeek

class MenuService:
    def __init__(self, menu_repository: MenuRepository):
        self.menu_repository = menu_repository

    def create_menu(self, restaurant_id: int, day: DayOfWeek, menu: MenuCreate):
        return self.menu_repository.create_menu(restaurant_id, day, menu)

    def get_menu(self, restaurant_id: int, day: DayOfWeek):
        return self.menu_repository.get_menu(restaurant_id, day)

    def update_menu(self, restaurant_id: int, day: DayOfWeek, menu: MenuUpdate):
        return self.menu_repository.update_menu(restaurant_id, day, menu)

    def delete_menu(self, restaurant_id: int, day: DayOfWeek):
        return self.menu_repository.delete_menu(restaurant_id, day)