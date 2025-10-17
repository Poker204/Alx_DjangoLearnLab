# api/models.py
from django.db import models

# Model: Author
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Model: Book
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # ForeignKey to Author. 'related_name' is critical for the nested serializer.
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books' 
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"