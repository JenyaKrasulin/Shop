from django.shortcuts import render, get_object_or_404
from django.core.cache import cache


class MixinView:
    template = None
    context = None

    def get(self, request):
        return render(request, self.template, self.context)


class MixinNeededView:
    template = None
    context = None
    model = None
    name=None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        self.context[self.model.__name__.lower()] = obj
        return render(request, self.template, context=self.context)


