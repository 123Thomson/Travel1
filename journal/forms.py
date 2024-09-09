from django import forms
from .models import TravelEntry

class TravelEntryForm(forms.ModelForm):
    class Meta:
        model = TravelEntry
        fields = ['title', 'content', 'location', 'photos']
