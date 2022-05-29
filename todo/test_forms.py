from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    # test to check the name field is correctly filled in
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

# test to check if the done attribute is not required

    def test_item_done_field_is_not_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())

# test to check if location field is required

    def test_item_location_is_required(self):
        form = ItemForm({'location': ''})
        self.assertFalse(form.is_valid())
