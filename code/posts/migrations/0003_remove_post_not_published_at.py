# Generated by Django 5.1.5 on 2025-01-20 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0002_post_not_published_at_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='not_published_at',
        ),
    ]
