from django.contrib import admin
from .models import Chapter, Exercise

# Define the inline admin descriptor for Exercise model
class ExerciseInline(admin.TabularInline):  # or admin.StackedInline for a stacked layout
    model = Exercise
    extra = 1  # Number of empty forms to display initially

# Register Chapter model with the inline Exercise model
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_name', 'subject')
    inlines = [ExerciseInline]  # Add ExerciseInline here

# Register Exercise model separately if needed
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_title', 'chapter')
    list_filter = ('chapter',)  # Optional: Adds a filter sidebar for chapters
