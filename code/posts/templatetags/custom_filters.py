from django import template

from posts.models import Post

register = template.Library()


@register.filter
def to_uppercase(value: str):
    if not isinstance(value, str):
        return value

    return value.capitalize()


@register.filter
def remove_a_letters(value: str):
    if not isinstance(value, str):
        return value

    return value.replace('e', '')


@register.filter
def to_lowercase(value: str):
    if not isinstance(value, str):
        return value

    return value.lower()


@register.simple_tag
def get_article_content(article: Post):
    if article.author.id == 20:
        return f'{article.title} by Admin'

    return article.content
