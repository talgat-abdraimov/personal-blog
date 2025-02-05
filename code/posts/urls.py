from django.urls import path
from django.views.generic import TemplateView

from .views import ArticleView, ContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index_page'),
    path('articles/', ArticleView.as_view(), name='articles_page'),
    path('articles/<str:slug>/', ArticleView.as_view(), name='article_detail'),
    path('about-us/', TemplateView.as_view(template_name='posts/about.html'), name='about_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
]
