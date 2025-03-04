from fastapi import APIRouter, Depends, HTTPException
from app.services.menu import MenuService
from app.repositories.menu import MenuRepository
from app.core.database import get_db
from app.schemas.menu import MenuCreate, MenuUpdate
from app.core.dependencies import get_current_restaurant, get_authorized_user
from app.models.menu import DayOfWeek

router = APIRouter()

class MenuController:
    def __init__(self, db=Depends(get_db)):
        self.menu_service = MenuService(MenuRepository(db))

    def _obtain_menu_by_id(self, restaurant_id, day):
        db_menu = self.menu_service.get_menu(restaurant_id, day)
        if db_menu is None:
            raise HTTPException(status_code=404, detail="Menu not found")
        return db_menu

    def get_menu_or_404(self, restaurant_id: int, day: DayOfWeek, current_user: dict):
        db_menu = self._obtain_menu_by_id(restaurant_id, day)
        if db_menu.restaurant_id != current_user["id"]:
            raise HTTPException(status_code=403, detail="Forbidden")
        return db_menu
        
    def create_menu(self, restaurant_id: int, menu: MenuCreate, current_user: dict = Depends(get_current_restaurant)):
        existing_menu = self.menu_service.get_menu(restaurant_id, menu.day)
        if existing_menu:
            raise HTTPException(status_code=400, detail="Menu for this day already exists")
        return self.menu_service.create_menu(restaurant_id, menu.day, menu)

    def get_menu(self, restaurant_id: int, day: DayOfWeek, current_user: dict = Depends(get_authorized_user)):
        db_menu = self._obtain_menu_by_id(restaurant_id, day)
        return db_menu

    def update_menu(self, restaurant_id: int, day: DayOfWeek, menu: MenuUpdate, current_user: dict = Depends(get_current_restaurant)):
        self.get_menu_or_404(restaurant_id, day, current_user)
        return self.menu_service.update_menu(restaurant_id, day, menu)

    def delete_menu(self, restaurant_id: int, day: DayOfWeek, current_user: dict = Depends(get_current_restaurant)):
        self.get_menu_or_404(restaurant_id, day, current_user)
        return self.menu_service.delete_menu(restaurant_id, day)

def get_controller(db=Depends(get_db)):
    return MenuController(db)

@router.post("/", response_model=MenuCreate)
def create_menu(menu: MenuCreate, controller: MenuController = Depends(get_controller)):
    return controller.create_menu(menu.restaurant_id, menu)

@router.get("/{restaurant_id}/{day}", response_model=MenuCreate)
def get_menu(restaurant_id: int, day: DayOfWeek, controller: MenuController = Depends(get_controller)):
    return controller.get_menu(restaurant_id, day)

@router.put("/{restaurant_id}/{day}", response_model=MenuCreate)
def update_menu(restaurant_id: int, day: DayOfWeek, menu: MenuUpdate, controller: MenuController = Depends(get_controller)):
    return controller.update_menu(restaurant_id, day, menu)

@router.delete("/{restaurant_id}/{day}")
def delete_menu(restaurant_id: int, day: DayOfWeek, controller: MenuController = Depends(get_controller)):
    return controller.delete_menu(restaurant_id, day)