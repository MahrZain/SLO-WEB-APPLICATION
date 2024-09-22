from django.db import models

# Create your models here.
class Home(models.Model):
    heading = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)