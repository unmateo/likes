from django.contrib import admin

# Register your models here.
from .models import Item, Tag, ItemTag


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]
    list_display = ["id", "created_at", "updated_at"]

class ItemTagsInline(admin.TabularInline):
    model = Item.tags.through

class ItemAdmin(BaseAdmin):
    inlines = [ItemTagsInline]
    list_display = BaseAdmin.list_display  + ["name"]

class TagAdmin(BaseAdmin):
    inlines = [ItemTagsInline]
    list_display = BaseAdmin.list_display  + ["name"]

class ItemTagAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["item", "tag"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
