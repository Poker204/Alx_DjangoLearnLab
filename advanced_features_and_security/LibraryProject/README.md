# LibraryProject

## Overview
This Django project demonstrates:

- Custom User Model (`CustomUser`) with `date_of_birth` and `profile_photo`
- Book model with custom permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
- Groups: `Viewers`, `Editors`, `Admins` with appropriate permissions
- Views protected with `@permission_required` decorators

## Permissions and Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run the server: `python manage.py runserver`
5. Access the admin site to manage users and groups

## Notes
- Custom user model is defined in `bookshelf/models.py`
- Admin registration is in `bookshelf/admin.py`
- Views are in `bookshelf/views.py` with permission checks
