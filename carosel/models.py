from django.db import models

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carosel', help_text="Image size 1280 x 719 only")
    url = models.URLField(max_length=200, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    