from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        error_messages={'unique': 'Поезд с таким названием уже существует'},
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Введите название поезда'})
    )

    travel_time = forms.IntegerField(
        label='Время в пути/ч',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Введите время в пути/ч'})
    )

    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='Город отправления',
        widget=forms.Select(attrs={'class': 'form-control mb-3 js-example-basic-single'})
    )

    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='Город прибытия',
        widget=forms.Select(attrs={'class': 'form-control mb-3 js-example-basic-single'})
    )

    class Meta:
        model = Train
        fields = '__all__'
