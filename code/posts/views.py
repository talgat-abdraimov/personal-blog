from django.shortcuts import render

from .models import Post


def about(request):
    return render(request, 'posts/about.html')


def articles(request):
    articles_list = Post.objects.all()

    return render(request, 'posts/article-list.html', context={'articles': articles_list})


def article_detail(request, slug: str):
    article = Post.objects.get(slug=slug)

    return render(request, 'posts/article-detail.html', context={'article': article})


def index(request):
    return render(request, 'base.html', context={'name': 'John Doe'})
