from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
     path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
 ["books/create", "books/update", "books/delete"]
