# advanced_features_and_security/LibraryProject/relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('example/', views.example_function_view, name='example-function'),

    # Class-based view
    path('example-class/', views.ExampleClassView.as_view(), name='example-class'),
    from .views import list_books", "LibraryDetailView"]
]
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=
