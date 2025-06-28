from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.menu_item1 = MenuItem.objects.create(
            title='Pasta Carbonara',
            price=12.99,
            inventory=10
        )

        self.menu_item2 = MenuItem.objects.create(
            title='Pizza Margherita',
            price=15.50,
            inventory=5
        )

        self.menu_item3 = MenuItem.objects.create(
            title='Caesar Salad',
            price=8.75,
            inventory=20
        )

    def test_getall(self):
        url = '/restaurant/menu/'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_items = MenuItem.objects.all()

        serializer = MenuItemSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)

        self.assertEqual(len(response.data), 3)

        titles = [item['title'] for item in response.data]
        self.assertIn('Pasta Carbonara', titles)
        self.assertIn('Pizza Margherita', titles)
        self.assertIn('Caesar Salad', titles)
