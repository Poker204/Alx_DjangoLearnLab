# LibraryProject/LibraryProject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # custom user app
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'
["DEBUG", "SECURE_BROWSER_XSS_FILTER", "X_FRAME_OPTIONS", "SECURE_CONTENT_TYPE_NOSNIFF", "CSRF_COOKIE_SECURE", "SESSION_COOKIE_SECURE"]
