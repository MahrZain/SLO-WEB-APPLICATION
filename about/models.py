from django.db import models

# Create your models here.
class  About(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name