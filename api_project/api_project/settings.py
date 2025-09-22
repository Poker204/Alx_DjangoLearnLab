INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",   # <-- Add this
    "api",              # <-- Your app
    rest_framework.authtoken
    rest_framework.authentication.TokenAuthentication
    rest_framework.permissions.IsAuthenticated"
]
