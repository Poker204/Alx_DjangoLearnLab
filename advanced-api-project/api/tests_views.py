from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(title="Test Book", author="Lenin", publication_year=2024)
        self.list_url = reverse('book-list')  # update to match your URL name

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
