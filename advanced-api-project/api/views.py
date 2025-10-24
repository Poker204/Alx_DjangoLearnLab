from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create, everyone can read
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve, update, or delete a single book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can update/delete
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
            ["ListView", "DetailView", "UpdateView", "DeleteView"]
        return [permissions.AllowAny()]
["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
