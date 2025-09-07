from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register the models in the admin interface
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
