# advanced_features_and_security/LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm

# List all books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View a single book detail
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Example form view
@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
