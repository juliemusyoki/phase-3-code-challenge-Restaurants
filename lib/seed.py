# lib/seed.py
from sqlalchemy.orm import Session
from config import SessionLocal  
from models import Customer, Restaurant, Review

def seed_data(db: Session):
    # Create sample instances of Customer, Restaurant, and Review
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    restaurant1 = Restaurant(name="Tasty Bites", price=2)
    restaurant2 = Restaurant(name="Gourmet Grill", price=3)

    review1 = Review(star_rating=4, customer=customer1, restaurant=restaurant1)
    review2 = Review(star_rating=5, customer=customer1, restaurant=restaurant2)
    review3 = Review(star_rating=3, customer=customer2, restaurant=restaurant1)

    db.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2, review3])
    db.commit()

if __name__ == "__main__":
    # Run seed_data when this file is executed
    db = SessionLocal()
    seed_data(db)
    db.close()
