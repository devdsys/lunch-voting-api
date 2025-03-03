from app.models.restaurant import Restaurant
from app.core.database import SessionLocal
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate
from app.models import Restaurant

class RestaurantRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_restaurant(self, restaurant: RestaurantCreate):
        try:
            db_restaurant = Restaurant(name=restaurant.name, address=restaurant.address, working_hours=restaurant.working_hours, email=restaurant.email, password=restaurant.password)
            self.db.add(db_restaurant)
            self.db.commit()
            self.db.refresh(db_restaurant)
            return db_restaurant
        except Exception as e:
            self.db.rollback()
            raise e

    def get_restaurant(self, restaurant_id: int):
        return self.db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    def update_restaurant(self, restaurant_id: int, restaurant: RestaurantUpdate):
        db_restaurant = self.get_restaurant(restaurant_id)
        if db_restaurant:
            db_restaurant.name = restaurant.name
            db_restaurant.address = restaurant.address
            db_restaurant.working_hours = restaurant.working_hours
            self.db.commit()
            self.db.refresh(db_restaurant)
            return db_restaurant
        return None

    def delete_restaurant(self, restaurant_id: int):
        db_restaurant = self.get_restaurant(restaurant_id)
        if db_restaurant:
            self.db.delete(db_restaurant)
            self.db.commit()
            return {"message": "Restaurant deleted successfully"}
        return None

    def get_all_restaurants(self):
        return self.db.query(Restaurant).all()
    
    def get_user_by_email(self, email: str, ):
        return self.db.query(Restaurant).filter(Restaurant.email == email).first()