from django.shortcuts import render
from .models import Works

def home(request):
    works = Works.objects.all()
    context = {
        "works": works
    }

    return render(request, 'index.html', context)