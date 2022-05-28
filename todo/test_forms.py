from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form_is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        
    
    def test_item_done_is_required(self):
        form = ItemForm({'name': 'Learn'})
        self.assertTrue(form_is_valid())


    def test_item_location_is_required(self):
        form = ItemForm({'location': ''})
        self.assertTrue(form_is_valid())
    
    def test_item_location_form_no_data(self):
        form = ItemForm({''})
        self.assertFalse(form_is_valid())    