from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change a book's details"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
 ["class UserProfile(models.Model):", "Admin", "Librarian", "Member"]
