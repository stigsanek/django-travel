from django.urls import path

from cities.views import CityDetailView, CityListView

urlpatterns = [
    path('', CityListView.as_view(), name='city-list'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
]
