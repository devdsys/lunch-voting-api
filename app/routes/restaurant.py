from fastapi import APIRouter, Depends, HTTPException
from app.services.restaurant import RestaurantService
from app.repositories.restaurant import RestaurantRepository
from app.core.database import get_db
from app.schemas.restaurant import RestaurantCreate, Restaurant, RestaurantUpdate
from app.core.dependencies import get_current_restaurant, get_current_employee

router = APIRouter()

class RestaurantController:
    def __init__(self, db=Depends(get_db)):
        self.restaurant_service = RestaurantService(RestaurantRepository(db))

    def get_restaurant_or_404(self, restaurant_id: int, current_user: dict):
        db_restaurant = self.restaurant_service.get_restaurant(restaurant_id)
        if db_restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        if db_restaurant.email != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")
        return db_restaurant

    def create_restaurant(self, restaurant: RestaurantCreate):
        existing_restaurant = self.restaurant_service.get_restaurant(1)
        if existing_restaurant:
            raise HTTPException(status_code=400, detail="Restaurant with this name or address already exists")
        return self.restaurant_service.create_restaurant(restaurant)

    def get_restaurant(self, restaurant_id: int, current_user: dict = Depends(get_current_restaurant)):
        return self.get_restaurant_or_404(restaurant_id, current_user)

    def update_restaurant(self, restaurant_id: int, restaurant: RestaurantUpdate, current_user: dict = Depends(get_current_restaurant)):
        self.get_restaurant_or_404(restaurant_id, current_user)
        return self.restaurant_service.update_restaurant(restaurant_id, restaurant)

    def delete_restaurant(self, restaurant_id: int, current_user: dict = Depends(get_current_restaurant)):
        self.get_restaurant_or_404(restaurant_id, current_user)
        return self.restaurant_service.delete_restaurant(restaurant_id)

def get_controller(db=Depends(get_db)):
    return RestaurantController(db)

@router.post("/", response_model=Restaurant)
def create_restaurant(restaurant: RestaurantCreate, controller: RestaurantController = Depends(get_controller)):
    return controller.create_restaurant(restaurant)

@router.get("/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int, current_user: dict = Depends(get_current_restaurant), controller: RestaurantController = Depends(get_controller)):
    return controller.get_restaurant(restaurant_id, current_user)

@router.put("/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: int, restaurant: RestaurantUpdate, current_user: dict = Depends(get_current_restaurant), controller: RestaurantController = Depends(get_controller)):
    return controller.update_restaurant(restaurant_id, restaurant, current_user)

@router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: int, current_user: dict = Depends(get_current_restaurant), controller: RestaurantController = Depends(get_controller)):
    return controller.delete_restaurant(restaurant_id, current_user)

@router.get("/all", response_model=list[Restaurant])
def get_all_restaurants(current_user: dict = Depends(get_current_employee), db = Depends(get_db)):
    restaurant_service = RestaurantService(RestaurantRepository(db))
    return restaurant_service.get_all_restaurants()