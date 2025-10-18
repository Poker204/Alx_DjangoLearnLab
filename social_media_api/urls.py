from django.contrib import admin
from django.urls import path, include  # Make sure include is imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # include used here
]
