from django.contrib import admin
from .models import Home
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title','create_at')

admin.site.register(Home, HomeAdmin)