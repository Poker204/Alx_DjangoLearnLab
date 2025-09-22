# query_sample.py
from bookshelf.models import Book

# Example: Get all books
all_books = Book.objects.all()
print("All Books:", all_books)

# Example: Get books by a specific author
author_books = Book.objects.filter(author="J.K. Rowling")
print("Books by J.K. Rowling:", author_books)

# Example: Get a single book
try:
    single_book = Book.objects.get(id=1)
    print("Book with ID 1:", single_book)
except Book.DoesNotExist:
    print("Book with ID 1 does not exist")
Library.objects.get(name=library_name)", "books.all()
