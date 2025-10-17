# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

# Create a router instance
router = DefaultRouter()

# Register ViewSets (Assuming you have these defined in api/views.py)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

# The urlpatterns is a standard list that includes all generated routes
urlpatterns = [
    path('', include(router.urls)),
]