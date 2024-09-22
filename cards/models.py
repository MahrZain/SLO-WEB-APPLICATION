from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards', help_text="Image size 800 x 800 only")
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    # Validate image size
    def clean(self):
        if self.image:
            img = Image.open(self.image)
            if img.height != 800 or img.width != 800:
                raise ValidationError("The image must be 800x800 pixels.")
    
    # Optional: Override save method to automatically adjust image size if needed
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height != 800 or img.width != 800:
                raise ValidationError("Image dimensions should be 800x800 pixels.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
