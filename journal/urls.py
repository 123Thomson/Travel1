# journal/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),  # Logout view
    path('register/', views.registration_view, name='registration'),  # Registration view
    path('search/', views.search_view, name='search'),  # Search view
]
