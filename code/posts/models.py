from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название'))  # VARCHAR
    content = models.TextField(verbose_name=_('Контент'))  # TEXT
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # INT

    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated_at = models.DateTimeField(auto_now=True)  # DATETIME

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')


class Category(models.Model):
    name = models.CharField(max_length=120)
    posts = models.ManyToManyField(Post, related_name='categories')
