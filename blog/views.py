from .models import Topic
from django.shortcuts import render


def index(request):
    blogs = Topic.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

