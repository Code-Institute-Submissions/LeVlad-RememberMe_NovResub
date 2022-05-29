from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    # test to check if the done attribute defaults to False

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
        