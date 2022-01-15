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
        tags = Tag.objects.filter(name__icontains=query)
        context['tags'] = tags
        return context
