# seeds.py
from models import Restaurant, Customer, Review, session

# Add sample data
tasty_bites = Restaurant(name='Tasty Bites', price=2)
gourmet_grill = Restaurant(name='Gourmet Grill', price=3)

john_doe = Customer(first_name='John', last_name='Doe')
jane_smith = Customer(first_name='Jane', last_name='Smith')

review1 = Review(customer=john_doe, restaurant=tasty_bites, star_rating=4)
review2 = Review(customer=john_doe, restaurant=gourmet_grill, star_rating=5)
review3 = Review(customer=jane_smith, restaurant=tasty_bites, star_rating=3)

# Commit the changes
session.commit()
