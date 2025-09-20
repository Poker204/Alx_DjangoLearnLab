# Output is not directly returned, but the object is deleted from the database.
# To verify the deletion, we can attempt to retrieve the book again:
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book was successfully deleted.")  # Expected output
 ["book.delete", "from bookshelf.models import Book"]
