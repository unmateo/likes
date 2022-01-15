from django.views import generic

from .models import Item, Tag


class ItemListView(generic.ListView):
    model = Item
    template_name = "likes/pages/items.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "likes/pages/tags.html"
