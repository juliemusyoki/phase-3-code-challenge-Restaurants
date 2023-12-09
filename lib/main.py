# main.py
from models import Restaurant, Customer, Review, session

# Create instances of your classes and test your methods here

# Example: Print all restaurant names
restaurants = session.query(Restaurant).all()
print("Restaurants:")
for restaurant in restaurants:
    print(f"- {restaurant.name}")

# Example: Print all customer names
customers = session.query(Customer).all()
print("\nCustomers:")
for customer in customers:
    print(f"- {customer.full_name()}")

# Example: Print reviews
reviews = session.query(Review).all()
print("\nReviews:")
for review in reviews:
    print(f"{review.customer.full_name()} gave {review.restaurant.name} a rating of {review.star_rating} stars.")
