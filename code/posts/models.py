from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название'))  # VARCHAR
    content = models.TextField(verbose_name=_('Контент'))  # TEXT
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Дата публикации'))  # DATETIME

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # INT

    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated_at = models.DateTimeField(auto_now=True)  # DATETIME

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Название')  # Название категории

    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    posts = models.ManyToManyField(Post, related_name='categories')

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name
