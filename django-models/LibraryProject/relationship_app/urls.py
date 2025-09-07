from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # A list view to show all books
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
] ["add_book/", "edit_book/"]
