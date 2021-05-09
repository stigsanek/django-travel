from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        error_messages={'unique': 'Город с таким названием уже существует'},
        widget=forms.TextInput(attrs={'class': 'form-control mb-3','placeholder': 'Введите название города'})
    )

    class Meta:
        model = City
        fields = ('name',)
