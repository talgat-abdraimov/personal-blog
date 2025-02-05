from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Post


# get, post
class ArticleView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            if request.method.lower() == 'get' and 'slug' in kwargs:
                handler = getattr(self, 'get_detail', self.http_method_not_allowed)

            elif request.method.lower() == 'get':
                handler = getattr(self, 'list', self.http_method_not_allowed)

            else:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)

        else:
            handler = self.http_method_not_allowed

        return handler(request, *args, **kwargs)

    def list(self, request):
        articles = Post.objects.all()

        return render(request, 'posts/article-list.html', context={'articles': articles})

    def get_detail(self, request, slug: str):
        article = Post.objects.get(slug=slug)

        form = ContactForm()

        return render(request, 'posts/article-detail.html', context={'article': article, 'form': form})


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'
    success_message = 'Thank you for your message!'
