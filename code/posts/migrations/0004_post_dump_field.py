# Generated by Django 5.1.5 on 2025-01-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0003_remove_post_not_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dump_field',
            field=models.DateField(null=True),
        ),
    ]
