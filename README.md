# SQLAlchemy
#### **By Juliet Musyoki **
This project is a solution to the Phase 3 Code Challenge for a restaurant review domain. It includes implementations of SQLAlchemy Migrations, Relationships, Class and Instance Methods, and Querying.

## Getting Started
These instructions will help you set up and run the project on your local machine.

### Prerequisites
Make sure you have Python and Pipenv installed on your machine.
   - Commands used earlier - Remember I already created migrations and models
        - ```pipenv install alembic``` => Installs Alembic package for database migrations
        - ```alembic init alembic``` => Initializes Alembic, creates the necessary configuration files and directories 
        - ```alembic revision --autogenerate -m "initial"``` => Generates an automatic migration script with a message "initial" - after which you add your code for perfoming operations on your db
        - ```alembic upgrade head``` - Applies the generated migration script to update the database to the latest version 


## Setup/Installation Requirements
    - Download a file in the code section to the desired folder
    - Extract the files
    - Open the folder with vs code.
    - Activate the virtual environment in the terminal using ```pipenv shell``` command them ```pipenv install```
   
## Folder Structure
├── alembic
│ ├── versions # Database migration scripts
│ ├── env.py # Alembic environment configuration
│ └── script.py.mako
├── lib
│ ├── config.py # Database configuration
│ ├── main.py # Main application logic
│ ├── models.py # SQLAlchemy model definitions
│ ├── seed.py # Seed data for testing
│ └── tests.py # Unit tests
├── .gitignore # Git ignore file
├── README.md # Project documentation
└── database.sqlite # SQLite database file

  Initialize the Database: Run the following commands to create and migrate the database.

  - ``` alembic upgrade head
``` 
- ```python3 lib/seed.py
``` Populate the database with sample data.
  - ```python3 lib/tests.py``` to run example tests
  

### License
*Licenced under the MIT licence
Free of use