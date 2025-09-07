# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to the home page (or any page you prefer)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'  # Use the custom login template

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'  # Use the custom logout template
