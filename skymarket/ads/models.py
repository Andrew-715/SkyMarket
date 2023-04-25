from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='ad_pictures/')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text
