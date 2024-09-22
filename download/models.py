from django.db import models

class downlaod(models.Model):  # Consider renaming to capitalize "Download"
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='download',null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:  # Corrected class name
        verbose_name = 'download'
        verbose_name_plural = 'downloads'
