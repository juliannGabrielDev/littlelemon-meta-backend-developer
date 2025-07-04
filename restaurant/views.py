from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
