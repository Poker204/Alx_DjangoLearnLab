from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # 🔍 Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 🧩 Filtering fields
    filterset_fields = ['title', 'author', 'published_date']

    # 🔎 Search fields (partial text matching)
    search_fields = ['title', 'author']

    # 🔢 Ordering fields
    ordering_fields = ['title', 'published_date']

    # Default ordering (optional)
    ordering = ['title']

    # Custom permission logic for create (optional)
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

 ["from django_filters import rest_framework"]
