from django.db import models
from apps.movies.models import Movie
from apps.halls.models import Hall

STATUS_CHOICES = [
    ('active', 'Активен'),
    ('cancelled', 'Отменен')
]

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='Зал')
    data = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    price = models.DecimalField( max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'

    def __str__(self):
        return f'{self.movie.title} | {self.data} {self.time}'