# models.py
from django.db import models

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    # You might want to add additional fields like `alt_text` or `title` if needed

    def __str__(self):
        return "Logo"  # Return a meaningful name or identifier
