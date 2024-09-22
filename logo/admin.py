from django.contrib import admin
from .models import Logo
# Register your models here.
class LogoAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(Logo, LogoAdmin)
