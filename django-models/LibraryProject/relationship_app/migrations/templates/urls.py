from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL to list all books
    # Add more paths as necessary
]
