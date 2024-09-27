from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', include('contact.urls'), name='contact'),
    path('download/', views.download, name='download'),
    path('Subjects/<slug:slug>/', views.subject_detail, name='subject_detail'),
    path('Subjects/<slug:slug>/chapters/', views.subject_chapters, name='subject_chapters'),  
    path('chapters/', include('chapters.urls')), 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
