from django.contrib import admin

# Register your models here.
from .models import Item, Tag

admin.site.register({
    Item,
    Tag,
})
