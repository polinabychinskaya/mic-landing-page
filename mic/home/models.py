from django.db import models

# Create your models here.
class Article(models.Model):
    picture = models.ImageField(
        verbose_name='Article picture - Картинка',
        upload_to='uploads/%Y/%m/%d/'
    )

    title = models.CharField(
        verbose_name='Title - Заголовок',
        max_length=256
    )

    body = models.TextField(
        verbose_name='Main body - Содержание',
        max_length=10000
    )

    created = models.DateTimeField(
        verbose_name='Created - Создано',
        auto_now_add=True,
        auto_now=False
    )

    updated = models.DateTimeField(
        verbose_name='Updated - Обновлено',
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self):
        return self.title
    
