from django.urls import path
from .views import entry_list, entry_create

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('new/', entry_create, name='entry_create'),
]
