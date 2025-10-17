# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer with Custom Validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    # Custom Validation: Check that the publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value

# AuthorSerializer with Nested Books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested field using BookSerializer (many=True for the one-to-many relationship)
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']