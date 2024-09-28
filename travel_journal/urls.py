# travel_journal/urls.py

from django.contrib import admin
from django.urls import path, include
from journal import views  # Import the index view from the journal app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL to the index page
    path('journal/', include('journal.urls')),  # Additional URLs if needed
]
