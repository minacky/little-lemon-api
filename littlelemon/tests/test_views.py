from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setup(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory=60)
        self.menu3 = Menu.objects.create(title="Pasta", price=14.99, inventory=40)
        
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get(reverse('menuitem-list'))
        
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
