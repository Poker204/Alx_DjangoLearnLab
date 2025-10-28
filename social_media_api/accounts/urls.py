from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
