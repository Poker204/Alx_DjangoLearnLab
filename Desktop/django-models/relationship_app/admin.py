from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the author's name in the admin list view

# Register the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)  # Display title and author of the book
    search_fields = ('title', 'author__name')  # Allow search by title and author name

# Register the Library model
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the Librarian model
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')  # Display librarian name and the associated library

# Register your models with custom admin views
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)