# LibraryProject/LibraryProject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # custom user app
    bookshelf.CustomUser
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'
bookshelf.CustomUser
