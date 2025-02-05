from django.core.exceptions import ValidationError


def validate_no_forbidden_words(value: str):
    forbidden_words = ['spam', 'bad', 'nazik']

    if value.lower() in forbidden_words:
        raise ValidationError(f'Слово "{value}" запрещено в тексте')
