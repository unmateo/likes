from django.test import TestCase
from likes.models import Item, Tag


class ItemTestCase(TestCase):

    def test_item_name_is_uppercased(self):
        name = "test"
        item = Item.objects.create(name=name)
        self.assertEqual(item.name, name.upper())


class TagTestCase(TestCase):

    def test_tag_name_is_uppercased(self):
        name = "test"
        tag = Tag.objects.create(name=name)
        self.assertEqual(tag.name, name.upper())
