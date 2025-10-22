from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation to prevent future publication years.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.
    Includes a nested list of books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # `related_name='books'` used in Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
