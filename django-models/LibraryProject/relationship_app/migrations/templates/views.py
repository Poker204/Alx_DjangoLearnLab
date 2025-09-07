from django.shortcuts import render
from .models import Book

def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template with the list of books
    return render(request, 'relationship_app/list_books.html', {'books': books})
