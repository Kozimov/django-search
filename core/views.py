from django.shortcuts import render
from .models import Works

def home(request):
    if 'search' in request.GET:
        search_word = request.GET['search']
        works = Works.objects.filter(name__icontains=search_word)
    else:
        works = Works.objects.all()

    context = {
        "works": works
    }
    return render(request, 'index.html', context)