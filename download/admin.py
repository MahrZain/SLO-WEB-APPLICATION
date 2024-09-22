from django.contrib import admin
from .models import downlaod
# Register your models here.
class downAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'url')
admin.site.register(downlaod, downAdmin)
