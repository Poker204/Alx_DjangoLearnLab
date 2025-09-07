from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author():
    author_name = "George Orwell"  # Example author
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

# 2. List all books in a library
def books_in_library():
    library_name = "Central Library"  # Example library name
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

# 3. Retrieve the librarian for a library
def librarian_for_library():
    library_name = "Central Library"  # Example library
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")

# Execute the functions to check the queries
if __name__ == "__main__":
    books_by_author()
    books_in_library()
    librarian_for_library()
