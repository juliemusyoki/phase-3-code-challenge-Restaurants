# lib/restaurant.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from lib.base import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Add relationships
    reviews = relationship("Review", back_populates="restaurant")
