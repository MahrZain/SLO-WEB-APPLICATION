from django.db import models
from subjects.models import Subjects
from category.models import Category 

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=100, null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='chapters', null=True, blank=False)  # New field for Category
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='chapters', null=True, blank=False)

    def __str__(self):
        return self.chapter_name

class Exercise(models.Model):
    exercise_title = models.CharField(max_length=100, null=True, blank=False)
    exercise_description = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='exercises', null=True, blank=False)

    def __str__(self):
        return self.exercise_title
