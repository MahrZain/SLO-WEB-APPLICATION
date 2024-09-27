from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from category.models import Category
from autoslug import AutoSlugField

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=16,help_text='max 16 characters', null=False, blank=False)
    description = models.TextField(max_length=75, null=True, blank=False,help_text='max 75 characters') 
    new_slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)
    image = models.ImageField(upload_to='cards', help_text="Image size 800 x 800 only")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    # Validate image size
    def clean(self):
        super().clean()  # Call the parent clean method first
        if self.image:
            img = Image.open(self.image)
            if img.height != 800 or img.width != 800:
                raise ValidationError("The image must be 800x800 pixels.")
            
            
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
