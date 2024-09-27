from django.urls import path
from .views import filter_subjects

urlpatterns = [
    path('filter-subjects/', filter_subjects, name='filter_subjects'),
]
