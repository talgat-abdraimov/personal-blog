from django.forms import CharField, EmailField, Form, Textarea

from .validators import validate_no_forbidden_words


class ContactForm(Form):
    name = CharField(max_length=100, label='Имя')
    email = EmailField(label='Укажите ваш email')
    message = CharField(widget=Textarea, label='Сообщение')


class CommentForm(Form):
    content = CharField(widget=Textarea, label='Текст комментария', validators=[validate_no_forbidden_words])
