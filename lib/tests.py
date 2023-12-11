# lib/tests.py
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Customer, Restaurant, Review

class TestRestaurantReviews(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.db = Session()
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        self.db.close()

    def test_customer_creation(self):
        customer = Customer(first_name="John", last_name="Doe")
        self.db.add(customer)
        self.db.commit()
        retrieved_customer = self.db.query(Customer).filter_by(first_name="John").first()
        self.assertEqual(retrieved_customer.last_name, "Doe")

    def test_restaurant_creation(self):
        restaurant = Restaurant(name="Tasty Bites", price=2)
        self.db.add(restaurant)
        self.db.commit()
        retrieved_restaurant = self.db.query(Restaurant).filter_by(name="Tasty Bites").first()
        self.assertEqual(retrieved_restaurant.price, 2)

    def test_review_creation(self):
        customer = Customer(first_name="John", last_name="Doe")
        restaurant = Restaurant(name="Tasty Bites", price=2)
        review = Review(star_rating=4, customer=customer, restaurant=restaurant)
        self.db.add_all([customer, restaurant, review])
        self.db.commit()
        retrieved_review = self.db.query(Review).filter_by(star_rating=4).first()
        self.assertEqual(retrieved_review.customer.first_name, "John")

    def test_customer_full_name(self):
        customer = Customer(first_name="John", last_name="Doe")
        self.db.add(customer)
        self.db.commit()
        retrieved_customer = self.db.query(Customer).filter_by(first_name="John").first()
        self.assertEqual(retrieved_customer.full_name(), "John Doe")

    def test_customer_favorite_restaurant(self):
        customer = Customer(first_name="John", last_name="Doe")
        restaurant1 = Restaurant(name="Tasty Bites", price=2)
        restaurant2 = Restaurant(name="Gourmet Grill", price=3)
        review1 = Review(star_rating=4, customer=customer, restaurant=restaurant1)
        review2 = Review(star_rating=5, customer=customer, restaurant=restaurant2)
        self.db.add_all([customer, restaurant1, restaurant2, review1, review2])
        self.db.commit()
        retrieved_customer = self.db.query(Customer).filter_by(first_name="John").first()
        self.assertEqual(retrieved_customer.favorite_restaurant(), restaurant2)

    # Add more tests for other methods in the Customer model

if __name__ == '__main__':
    unittest.main()
