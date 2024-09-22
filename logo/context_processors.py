# context_processors.py
from .models import Logo

def logo(request):
    return {'logo': Logo.objects.first()}  # Fetch the first logo from the database
