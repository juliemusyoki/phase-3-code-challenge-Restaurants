# lib/main.py
from sqlalchemy.orm import Session
from .config import SessionLocal
from .models import Customer, Restaurant, Review

def main():
    db = SessionLocal()

    # Create sample data (You can replace this with your actual application logic)
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    restaurant1 = Restaurant(name="Tasty Bites", price=2)
    restaurant2 = Restaurant(name="Gourmet Grill", price=3)

    review1 = Review(star_rating=4, customer=customer1, restaurant=restaurant1)
    review2 = Review(star_rating=5, customer=customer1, restaurant=restaurant2)
    review3 = Review(star_rating=3, customer=customer2, restaurant=restaurant1)

    db.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2, review3])
    db.commit()

    # Retrieve and print information (Replace with your actual queries and logic)
    customers = db.query(Customer).all()
    restaurants = db.query(Restaurant).all()
    reviews = db.query(Review).all()

    print("Customers:")
    for customer in customers:
        print(f"{customer.first_name} {customer.last_name} has {len(customer.reviews)} reviews.")

    print("\nRestaurants:")
    for restaurant in restaurants:
        print(f"{restaurant.name} has an average rating of {restaurant.calculate_average_rating()} stars.")

    print("\nReviews:")
    for review in reviews:
        print(f"{review.customer.full_name()} gave {review.restaurant.name} a rating of {review.star_rating} stars.")

    db.close()

if __name__ == "__main__":
    main()
