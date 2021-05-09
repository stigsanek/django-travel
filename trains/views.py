from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from trains.models import Train

__all__ = ('TrainListView', 'TrainDetailView')


class TrainListView(ListView):
    queryset = Train.objects.all()
    template_name = 'trains/list.html'
    paginate_by = 5


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'
