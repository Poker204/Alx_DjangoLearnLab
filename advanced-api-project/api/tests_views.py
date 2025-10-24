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
class BookAPITestCase(APITestCase):
    """Tests for the Book API endpoints."""

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create test books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William Vincent",
            description="Introductory Django guide",
            published_date="2021-01-10"
        )
        self.book2 = Book.objects.create(
            title="Python Tricks",
            author="Dan Bader",
            description="Cool Python features",
            published_date="2020-05-22"
        )

        # API client
        self.client = APIClient()
        self.list_url = reverse('book-list-create')

    # ------------------- CREATE -------------------
    def test_create_book_authenticated(self):
        """Authenticated users can create a book."""
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "New Book",
            "author": "John Doe",
            "description": "A test book",
            "published_date": "2023-07-01"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book."""
        data = {"title": "Unauthorized", "author": "Nobody", "published_date": "2024-01-01"}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------- READ -------------------
    def test_list_books(self):
        """Anyone can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book."""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ------------------- UPDATE -------------------
    def test_update_book_authenticated(self):
        """Authenticated users can update a book."""
        self.client.login(username="testuser", password="testpass123")
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Updated Django Book"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_update_book_unauthenticated(self):
        """Unauthenticated users cannot update a book."""
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Hack Attempt"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------- DELETE -------------------
    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book."""
        self.client.login(username="testuser", password="testpass123")
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete a book."""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
