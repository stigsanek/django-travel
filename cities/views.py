from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import CityForm
from cities.models import City

__all__ = ('CityListView', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView')


class CityListView(ListView):
    queryset = City.objects.all()
    template_name = 'cities/list.html'


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    # success_url = reverse_lazy('cities:list')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:list')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:list')

    # if you don't need confirmation
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
