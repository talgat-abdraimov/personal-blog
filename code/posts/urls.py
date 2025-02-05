from django.urls import path
from django.views.generic import TemplateView

from .views import ArticleCreateView, ArticleDetailView, ArticleListView, ContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index_page'),
    path('articles/', ArticleListView.as_view(), name='articles_page'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<str:human_readable_title>/', ArticleDetailView.as_view(), name='article_detail'),
    path('about-us/', TemplateView.as_view(template_name='posts/about.html'), name='about_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
]
