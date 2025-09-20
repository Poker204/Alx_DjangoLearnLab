from django.db import models

# Author Model: Defines the Author with a name
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book Model: Defines the Book with a title and a ForeignKey to the Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author

    def __str__(self):
        return self.title

# Library Model: Defines a Library with a name and ManyToMany relationship with Books
class Library(models.Model):
    name = models.CharField(max_length=100)  # Library's name
    books = models.ManyToManyField(Book)  # ManyToMany relationship with Book

    def __str__(self):
        return self.name

# Librarian Model: Defines a Librarian with a name and OneToOne relationship with Library
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Librarian's name
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # OneToOne relationship with Library

    def __str__(self):
        return self.name
