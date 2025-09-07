# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# Function-based view (Already added for listing books)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # To access the object in the template as 'library'
    
    # Optionally, you can define a custom get_context_data to include additional data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books related to this specific library
        context['books'] = self.object.books.all()  # Assuming 'books' is a ManyToMany relationship
        return context
