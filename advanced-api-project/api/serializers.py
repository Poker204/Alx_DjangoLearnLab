from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for the Book model
# Serializes all fields and includes validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation method for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
# Includes the author's name and a nested list of their books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for books related to this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
