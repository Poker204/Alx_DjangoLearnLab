Alx Django Learn Lab
Project Description

This Django project aims to teach fundamental Django concepts, including model creation, CRUD operations, and interacting with the Django admin interface. The Bookshelf app within the project helps manage a collection of books with various attributes such as title, author, and publication year.
Installation

Clone the repository:

git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

Install dependencies:

pip install -r requirements.txt

Run migrations to set up the database:

python manage.py migrate

Create a superuser to access the Django admin:

python manage.py createsuperuser

Run the Django development server:

python manage.py runserver

    Access the Django admin at http://127.0.0.1:8000/admin and log in using your superuser credentials.

Usage

    The project includes a Bookshelf app for managing books.
    Books can be added, retrieved, updated, and deleted using the Django admin interface.
    The admin interface allows you to search, filter, and manage book entries.

Contributing

Feel free to fork this repository and submit pull requests. Ensure you follow the contribution guidelines.
License
MIT License
