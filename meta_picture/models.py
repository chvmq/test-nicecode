from django.db import models
from django.urls import reverse


class Image(models.Model):
    """Модель картинки"""
    title = models.CharField('Название картинки', max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse(viewname='detail_photo', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ImageMetaData(models.Model):
    """Метаданные картинки"""
    image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Картинка')
    high = models.CharField('Высота', max_length=10)
    width = models.CharField('Ширина', max_length=10)
    average_color = models.CharField('Средний цвет картинки', max_length=255)
    number_of_coins = models.PositiveSmallIntegerField('Количество монет', blank=True, null=True)
    sum_of_coins = models.PositiveSmallIntegerField('Сумма монет', blank=True, null=True)

    def __str__(self):
        return self.image
