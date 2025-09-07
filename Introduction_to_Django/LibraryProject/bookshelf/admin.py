# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Create a custom admin class to display Book data with enhancements
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for author and publication year in the admin sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)
