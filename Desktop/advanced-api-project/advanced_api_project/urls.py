# advanced_api_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the API routes under the 'api/' prefix
    path('api/', include('api.urls')),
]