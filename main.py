# main.py
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

# Creating customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Creating restaurants
restaurant1 = Restaurant("Tasty Bites", 10)
restaurant2 = Restaurant("Gourmet Grill", 15)

# Adding reviews
review1 = customer1.add_review(restaurant1, 4)
review2 = customer1.add_review(restaurant2, 5)
review3 = customer2.add_review(restaurant1, 3)

# Displaying information
print("Customers:")
for customer in [customer1, customer2]:
    print(f"{customer.full_name()} has {len(customer.reviews)} reviews.")

print("\nRestaurants:")
for restaurant in [restaurant1, restaurant2]:
    avg_rating = sum([review.rating for review in restaurant.reviews]) / len(restaurant.reviews) if restaurant.reviews else 0
    print(f"{restaurant.name} has an average rating of {avg_rating} stars.")

print("\nReviews:")
for review in Review.all_reviews():
    print(review)
