# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView  # Correct import for DetailView
from .models import Library, Book

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # To access the object as 'library' in the template
    
    # Optionally, you can define a custom get_context_data method to add more context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books for this library
        return context
