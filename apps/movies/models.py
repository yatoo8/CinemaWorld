from django.db import models

class Movie(models.Model):
    STATUS_CHOICES = [
        ('showing', 'В прокате'),
        ('soon', 'Скоро'),
        ('archive', 'Архив'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название')
    poster = models.ImageField(upload_to='posters/',verbose_name='Постер')
    description = models.TextField(verbose_name='Описание')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    duration = models.PositiveIntegerField(verbose_name='Длительность (мин)')
    age_limit = models.PositiveIntegerField(verbose_name='Возрастное ограничение')
    language = models.CharField(max_length=50, verbose_name='Язык')
    trailer = models.URLField(verbose_name='Трейлер (Youtube)')
    release_start = models.DateField(verbose_name='Дата начала проката')
    release_end = models.DateField(verbose_name='Дата окончания проката')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='Статус')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title