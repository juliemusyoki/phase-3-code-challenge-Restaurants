# seeds.py
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review
from lib.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup SQLAlchemy engine and session
engine = create_engine('sqlite:///database.db')  # Adjust the connection string as needed
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

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
