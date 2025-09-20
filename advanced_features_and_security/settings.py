# settings.py

AUTH_USER_MODEL = 'accounts.CustomUser'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'LibraryProject.bookshelf',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom user app
    'accounts',
]
