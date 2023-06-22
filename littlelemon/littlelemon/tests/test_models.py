# test_models.py

from django.test import TestCase
# from .models import Menu
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description="Delicious ice cream")
        self.assertEqual(str(item), "IceCream : 80")
