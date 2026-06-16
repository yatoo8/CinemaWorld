from django.db import models

class Hall(models.Model):
    STATUS_CHOICES = [
        ('standart', 'Стандарт'),
        ('vip', 'VIP'),
        ('3d', '3D'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название')
    seats_count = models.PositiveIntegerField(verbose_name='Количество мест')
    hall_type = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='Тип зала')
    scheme = models.ImageField(upload_to='halls/schemes/', verbose_name='Схема зала')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

    def __str__(self):
        return self.title