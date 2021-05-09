from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from trains.forms import TrainForm
from trains.models import Train

__all__ = ('TrainListView', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView')


class TrainListView(ListView):
    queryset = Train.objects.all()
    template_name = 'trains/list.html'
    paginate_by = 5


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:list')
    success_message = 'Город успешно создан'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:list')
    success_message = 'Город успешно отредактирован'


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:list')

    # if you don't need confirmation
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

