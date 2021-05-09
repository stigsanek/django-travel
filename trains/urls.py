from django.urls import path

from trains.views import *

urlpatterns = [
    path('', TrainListView.as_view(), name='list'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
]
