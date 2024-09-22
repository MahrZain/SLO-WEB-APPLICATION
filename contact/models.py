from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Usrinfo(models.Model):
    Phone = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    address = models.TextField(null=False, blank=False)
    map_info = models.TextField(null=True, blank=False)
    map_link = models.TextField(max_length=400,null=True, blank=False , help_text="Size: 1000 x 450 for embeded map")

    class Meta:
        verbose_name_plural = "Admin info's"
        verbose_name = "Admin info"

    def __str__(self):
        return self.email