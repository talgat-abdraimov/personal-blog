from datetime import datetime, timezone

from django.contrib import admin

from .models import Category, Post


class CatetoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1


class PublishedFilter(admin.SimpleListFilter):
    title = 'Статус публикации'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('published', 'Опубликовано'),
            ('draft', 'Черновик'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.filter(published_at__isnull=False)

        if self.value() == 'draft':
            return queryset.filter(published_at__isnull=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ('mark_as_published',)
    list_display = ('title', 'slug', 'status_display', 'published_at')

    inlines = (CatetoryInline,)

    ordering = ('-published_at',)
    search_fields = ('title', 'content')
    list_filter = (PublishedFilter, 'author', 'categories')

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'content')}),
        ('Дополнительная информация', {'fields': ('slug', 'published_at', 'author')}),
    )

    def status_display(self, obj: Post):
        return 'Опубликовано' if obj.published_at else 'Не опубликовано'

    status_display.short_description = 'Статус'

    def mark_as_published(self, request, queryset):
        queryset.update(published_at=datetime.now(timezone.utc))

    mark_as_published.short_description = 'Опубликовать'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('categories')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
