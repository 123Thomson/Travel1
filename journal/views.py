from django.shortcuts import render, redirect
from .models import TravelEntry
from .forms import TravelEntryForm  # Create this form in the next step

def entry_list(request):
    if request.user.is_authenticated:
        # Fetch the user's travel entries
        entries = TravelEntry.objects.filter(user=request.user)  # Assuming you have a ForeignKey to User in your model
    else:
        # Redirect to the login page or show a message
        return redirect('login')  # Redirect to the login view or show an appropriate message

    return render(request, 'journal/entry_list.html', {'entries': entries})

def entry_create(request):
    if request.method == 'POST':
        form = TravelEntryForm(request.POST, request.FILES)
        if form.is_valid():
            travel_entry = form.save(commit=False)
            travel_entry.user = request.user
            travel_entry.save()
            return redirect('entry_list')
    else:
        form = TravelEntryForm()
    return render(request, 'journal/entry_form.html', {'form': form})

def home(request):
    return render(request, 'journal/home.html')
