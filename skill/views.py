from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cards.models import Card
from carosel.models import Carousel
from download.models import downlaod
from about.models import About
from home.models import Home
from subjects.models import Subjects
from category.models import Category
from chapters.models import Chapter,Exercise


def home(request):
    card = Card.objects.all()
    carousel = Carousel.objects.all()
    home = Home.objects.all()
    cat = Category.objects.all()
    data = {
        "card": card,
        "carousel": carousel,
        "home": home,
        "category": cat,
        "active_nav": "home",
    }
    return render(request, "index.html", data)



def about(request):
    about = About.objects.all()
 

    return render(request, "about.html", {"about": about, "active_nav": "about"})


def contact(request):
    return render(request, "contact.html", {"active_nav": "contact"})


def download(request):
    download = downlaod.objects.all()
    return render(request, "app-download.html", {"download": download,"active_nav": "download"})


def subject_detail(request, slug):
    # Fetch the category using the slug
    category = get_object_or_404(Category, slug=slug)
    
    # Retrieve all subjects that belong to the retrieved category
    subjects = Subjects.objects.filter(category=category)
    
    # Prepare data to pass to the template
    data = {
        "subjects": subjects,
        "category": category,
    }
    return render(request, "Subjects.html", data)

def subject_chapters(request, slug):
    subject = get_object_or_404(Subjects, slug=slug)
    chapters = subject.chapters.all()
    
    context = {
        'subject': subject,
        'chapters': chapters,
    }
    return render(request, 'chapters.html', context)
