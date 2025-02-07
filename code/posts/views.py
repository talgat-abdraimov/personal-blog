from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import ContactForm
from .models import Post

# ListView, DetailView, CreateView # UpdateView, DeleteView


class ArticleListView(ListView):
    model = Post
    template_name = 'posts/article-list.html'
    context_object_name = 'posts'
    paginate_by = 1
    queryset = Post.objects.filter(published_at__isnull=False)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article-detail.html'
    context_object_name = 'article'
    slug_field = 'human_readable_title'
    slug_url_kwarg = 'human_readable_title'


class ArticleCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'author')
    template_name = 'posts/article-create.html'
    success_url = '/articles/'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'
