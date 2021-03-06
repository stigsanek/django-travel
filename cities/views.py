from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from cities.forms import CityForm
from cities.models import City

__all__ = ('CityListView', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView')


class CityListView(ListView):
    queryset = City.objects.all()
    template_name = 'cities/list.html'
    paginate_by = 5


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:list')
    success_message = 'Город успешно создан'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:list')
    success_message = 'Город успешно отредактирован'


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:list')

    # if you don't need confirmation
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
