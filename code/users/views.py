from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('admin:login')
    template_name = 'users/signup.html'
