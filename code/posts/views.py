from datetime import datetime

from django.shortcuts import render


def index(request):
    published_at = datetime.now()

    author = {'first_name': 'John', 'l': 'Doe'}

    posts = [
        {
            'title': 'First post',
            'text': 'This is my',
        },
        {
            'title': 'Second post',
            'text': 'This is my second post',
        },
        {
            'title': 'Third post',
            'text': 'This is my third post',
        },
    ]
    return render(
        request,
        'posts/posts-list.html',
        context={'author': author, 'publish_date': published_at, 'posts': posts},
    )
