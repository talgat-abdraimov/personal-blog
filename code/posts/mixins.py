from django.http import HttpResponseForbidden


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(content='You need to be authenticated to view this page.')

        if request.user != self.get_object().author:
            return HttpResponseForbidden(content='You need to be the author of this post to view this page.')

        return super().dispatch(request, *args, **kwargs)
