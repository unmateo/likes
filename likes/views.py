from django.db.models import Count
from django.views import generic

from .models import Item, Tag


class HomeView(generic.TemplateView):
    template_name = "likes/pages/home.html"


class ItemListView(generic.ListView):
    model = Item
    template_name = "likes/pages/items.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = "likes/pages/tags.html"


class SearchView(generic.TemplateView):
    template_name = "likes/pages/tags.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = context['query']
        q = Tag.objects.annotate(items_count=Count("items"))
        tags = q.filter(name__icontains=query, items_count__gt=0)
        context['tags'] = tags
        return context
