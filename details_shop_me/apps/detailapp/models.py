from django.db import models
from django.urls import reverse


class Details(models.Model):
    """"Сами детали от определенной марки автомобиля"""
    name = models.CharField(max_length=255, db_index=True,
                            verbose_name='Название')
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y')
    published_or_not = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """"Ссылка на деталь"""
        return reverse('detail', kwargs={'detail_slug': self.slug})

    class Meta:
        ordering = ['time_create', ]


class Category(models.Model):
    """"Модель категории деталей АКПП, подвеска, шины и тд"""
    name = models.CharField(max_length=255, db_index=True,
                            verbose_name='Категория')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """"Ссылка на категорию"""
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        ordering = ['id', ]
