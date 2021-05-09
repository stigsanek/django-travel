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

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
