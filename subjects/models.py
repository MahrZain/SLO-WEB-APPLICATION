from django.db import models
from category.models import Category
from autoslug import AutoSlugField
# Create your models here.
class Subjects(models.Model):
    subject_name = models.CharField(max_length=10, help_text='max 10 character')
    subject_description = models.TextField(max_length=60, help_text='max 60 character')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='subjects', null=True, help_text="Image size 800 x 800 only")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='subject_name', unique=True, null=True, default=None)
    
    def __str__(self):
        return self.subject_name