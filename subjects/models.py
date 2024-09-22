from django.db import models
from category.models import Category
# Create your models here.
class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='subjects', null=True, help_text="Image size 800 x 800 only")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject_name