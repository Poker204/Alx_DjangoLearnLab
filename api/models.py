from django.db import models

class Author(models.Model):
    """
    Author model stores author details.
    Each author can have multiple books (One-to-Many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model represents individual books.
    Each book is associated with a single author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
