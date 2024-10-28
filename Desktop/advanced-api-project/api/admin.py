from django.contrib import admin
from .models import Author, Book

# Register models so they can be managed via Django admin
admin.site.register(Author)
admin.site.register(Book)
