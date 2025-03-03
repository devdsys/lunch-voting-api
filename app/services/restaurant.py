from app.repositories.restaurant import RestaurantRepository
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate

class RestaurantService:
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def create_restaurant(self, restaurant: RestaurantCreate):
        return self.restaurant_repository.create_restaurant(restaurant)

    def get_restaurant(self, restaurant_id: int):
        return self.restaurant_repository.get_restaurant(restaurant_id)

    def update_restaurant(self, restaurant_id: int, restaurant: RestaurantUpdate):
        return self.restaurant_repository.update_restaurant(restaurant_id, restaurant)

    def delete_restaurant(self, restaurant_id: int):
        return self.restaurant_repository.delete_restaurant(restaurant_id)

    def get_all_restaurants(self):
        return self.restaurant_repository.get_all_restaurants()