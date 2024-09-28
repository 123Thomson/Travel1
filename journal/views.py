# journal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView  # Make sure to import LoginView

# View to load the index page
def index(request):
    return render(request, 'journal/index.html')

# View for user registration
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user
            return redirect('index')  # Redirect to index after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Custom login view using Django's LoginView
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


# View for search functionality
def search_view(request):
    query = request.GET.get('q')
    # Implement your search logic here, returning results as necessary
    return render(request, 'journal/search_results.html', {'query': query})  # Example result page
