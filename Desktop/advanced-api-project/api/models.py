from django.db import models

# Author model represents a book author in the database
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        # String representation of the Author, used in admin and elsewhere
        return self.name

# Book model represents a book in the database
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    
    # Year the book was published
    publication_year = models.IntegerField()
    
    # ForeignKey relationship links a Book to an Author
    # "related_name='books'" allows reverse access: author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        # String representation of the Book
        return self.title
