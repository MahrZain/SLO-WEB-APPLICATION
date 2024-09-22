from django.contrib import admin
from .models import Subjects
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('category','subject_name','created_at')
admin.site.register(Subjects, SubjectAdmin)