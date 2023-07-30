Car Parts Store
This is an online car parts store built using Python Flask and PostgreSQL. It allows users to browse and purchase car parts, as well as manage their orders and account information.

Features
User authentication and authorization
Product catalog with categories and search functionality
Shopping cart and checkout process
Order history and management
User profile management

Setup

1. Clone the repository to your local machine.
2. Install Poetry if you haven't already.
3. Open a terminal in the project root directory and run poetry install to install the dependencies.
4. Activate the virtual environment created by Poetry by running poetry shell.
5. Create a PostgreSQL database and update the settings.py file with your database credentials.
6. Run the following commands to create the database tables and seed the database with initial data:
python manage.py makemigrations
python manage.py migrate
7. Start the server using python manage.py runserver.

Requirements
Python 3
Poetry
Django
PostgreSQL
DRF
