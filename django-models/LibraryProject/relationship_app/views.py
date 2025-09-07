from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Admin view - Only accessible by users with 'Admin' role
@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'admin_view.html')
