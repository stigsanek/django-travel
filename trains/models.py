from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Поезд')
    travel_time = models.PositiveIntegerField(verbose_name='Время в пути/ч')
    from_city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE,
        related_name='from_city_set',
        verbose_name='Город отправления'
    )
    to_city = models.ForeignKey(
        to='cities.City',
        on_delete=models.CASCADE,
        related_name='to_city_set',
        verbose_name='Город прибытия'
    )

    def __str__(self):
        return self.name

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Город отправления не может быть равен городу прибытия')

        qs = Train.objects.filter(
            from_city=self.from_city,
            to_city=self.to_city,
            travel_time=self.travel_time
        ).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Поезд с указанными параметрами уже существует')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
