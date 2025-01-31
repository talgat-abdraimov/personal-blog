from django.urls import path

from .views import about, article_detail, articles, index

urlpatterns = [
    path('', index, name='index_page'),
    path('articles/', articles, name='articles_page'),
    path('articles/<str:slug>/', article_detail, name='article_detail'),
    path('about-us/', about, name='about_page'),
]
