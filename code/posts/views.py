from django.shortcuts import render


def about(request):
    return render(request, 'posts/about.html')


articles_list = [
    {'id': 1, 'title': 'First article', 'content': 'This is the first article content'},
    {'id': 2, 'title': 'Second article', 'content': 'This is the second article content'},
    {'id': 3, 'title': 'Third article', 'content': 'This is the third article content'},
]


def articles(request):
    return render(request, 'posts/article-list.html', context={'articles': articles_list})


def article_detail(request, article_id: int):
    for article in articles_list:
        if article['id'] == article_id:
            return render(request, 'posts/article-detail.html', context={'article': article})

    return render(request, 'posts/article-detail.html')


def index(request):
    return render(request, 'base.html', context={'name': 'John Doe'})
