from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    dob = models.DateField(null=True, blank=True, verbose_name='Дата рождения')  # dob - date of birth

    username = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    bio = models.TextField(null=True, blank=True, verbose_name='Биография')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Profile of {self.user.email}'
