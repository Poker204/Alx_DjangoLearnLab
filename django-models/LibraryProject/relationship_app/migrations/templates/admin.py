from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the admin list view

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display title, author, and publication year
    search_fields = ('title', 'author__name')  # Allow searching by title or author name
    list_filter = ('author',)  # Filter by author

# Register Library model
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field
    search_fields = ('name',)  # Allow searching by name of the library

# Register Librarian model
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')  # Display librarian's name and the associated library
    search_fields = ('name', 'library__name')  # Allow searching by librarian name or library name
