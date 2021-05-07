from django.views.generic import DetailView, ListView

from cities.models import City


class CityListView(ListView):
    # model = City
    queryset = City.objects.all()


class CityDetailView(DetailView):
    model = City
    # queryset = City.objects.all()
