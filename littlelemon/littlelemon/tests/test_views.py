# test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name="Pizza", price=12, menu_item_description="Delicious pizza")
        self.menu2 = Menu.objects.create(name="Burger", price=8, menu_item_description="Tasty burger")

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        # Add more assertions for serialized data if needed
