# lib/main.py
from sqlalchemy.orm import Session
from .config import SessionLocal
from .models import Customer, Restaurant, Review

def main():
    db = SessionLocal()

    # Your application logic goes here
    # Use db.query() to perform database operations

    db.close()

if __name__ == "__main__":
    main()
