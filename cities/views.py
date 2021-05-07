from django.shortcuts import render

from .models import City


def index(request):
    qs = City.objects.all()
    context = {'cities': qs}

    return render(request, 'cities/index.html', context)
