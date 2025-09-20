from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Field for the book's title
    author = models.CharField(max_length=100)  # Field for the book's author
    publication_year = models.IntegerField()  # Field for the year the book was published

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
