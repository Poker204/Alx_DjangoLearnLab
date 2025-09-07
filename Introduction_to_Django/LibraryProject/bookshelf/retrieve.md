# Retrieve Operation for the Book Model

## Command:

```python
from bookshelf.models import Book

# Retrieve all books (or one if you prefer)
books = Book.objects.all()  # Retrieve all books from the database
for book in books:
    print(book)

