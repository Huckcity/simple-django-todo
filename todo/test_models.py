from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    
    def test_done_defaults_to_false(self):
        
        item = Item(name="Create test")
        item.save()
        
        self.assertEqual(item.name, "Create test")
        self.assertEqual(item.done, False)
        
    def test_can_create_item_with_name_and_status(self):
        
        item = Item(name="Create test", done=True)
        item.save()
        
        self.assertEqual(item.name, "Create test")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        
        item = Item(name="Create test")
        self.assertEqual("Create test", str(item))