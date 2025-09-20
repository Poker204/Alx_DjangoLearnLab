# Retrieve Operation for the Book Model

## Command:

```python
from bookshelf.models import Book

# Retrieve the book with the title '1984'
book = Book.objects.get(title="1984")
print(book)
