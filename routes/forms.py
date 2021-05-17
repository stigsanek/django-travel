from django import forms

from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='Город отправления',
        widget=forms.Select(attrs={'class': 'form-control mb-3'})
    )

    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='Город прибытия',
        widget=forms.Select(attrs={'class': 'form-control mb-3'})
    )

    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        label='Через города',
        widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}),
        required=False
    )

    travelling_time = forms.IntegerField(
        label='Время в пути/ч',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Введите время в пути/ч'})
    )
