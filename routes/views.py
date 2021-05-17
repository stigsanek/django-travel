from django.contrib import messages
from django.shortcuts import render

from routes.forms import RouteForm
from routes.services import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)

        if form.is_valid():
            try:
                context = get_routes(form)
            except ValueError as err:
                messages.error(request, err)
                return render(request, 'routes/home.html', {'form': form})

            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')

        return render(request, 'routes/home.html', {'form': form})
