from django.shortcuts import render
from .models import Works
from django.db.models import Q

def home(request):
    if 'search' in request.GET:
        search_word = request.GET['search']
        full = Q(Q(name__icontains=search_word) | Q(surname__icontains=search_word) | Q(age__icontains=search_word) | Q(job__icontains=search_word))
        works = Works.objects.filter(full)
    else:
        works = Works.objects.all()

    context = {
        "works": works
    }
    return render(request, 'index.html', context)