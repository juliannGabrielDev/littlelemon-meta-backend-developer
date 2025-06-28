from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField()

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return (
            f"Booking for {self.name} on {self.booking_date.strftime('%Y-%m-%d')}"
        )


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return f"{self.title} - ${self.price}"
