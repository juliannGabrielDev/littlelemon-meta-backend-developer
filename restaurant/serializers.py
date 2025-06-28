from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'number_of_guests', 'booking_date']
        read_only_fields = ['id']

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        read_only_fields = ['id']
