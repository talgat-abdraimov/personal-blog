from datetime import datetime

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название'))  # VARCHAR
    content = models.TextField(verbose_name=_('Контент'))  # TEXT
    human_readable_title = models.SlugField(
        max_length=120, unique=True, verbose_name=_('Слаг'), null=True, blank=True
    )
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Дата публикации'))  # DATETIME

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')  # INT

    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated_at = models.DateTimeField(auto_now=True)  # DATETIME

    views = models.PositiveIntegerField(default=0, verbose_name=_('Просмотры'))  # INT

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.human_readable_title:
            self.human_readable_title = slugify(self.title)

        if not self.pk:
            self.published_at = datetime.now()

        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Название')  # Название категории

    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    posts = models.ManyToManyField(Post, related_name='categories')

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # INT

    content = models.TextField(verbose_name=_('Контент'))  # TEXT

    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated_at = models.DateTimeField(auto_now=True)  # DATETIME

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return f'{self.post}'
