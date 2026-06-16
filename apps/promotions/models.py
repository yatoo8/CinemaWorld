from django.db import models

class Promotion(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    valid_until = models.DateField(verbose_name='Срок действия')
    conditions = models.TextField(verbose_name='Условия')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title