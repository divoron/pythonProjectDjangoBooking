from django.db import models
from django.utils import timezone


# Create your models here.
class BookingRoom(models.Model):
    ordered_room = models.CharField(max_length=5)
    type_room = models.CharField(max_length=10, help_text='Economy/Semi-suite/Luxury')
    guest_name = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rental_days = models.IntegerField()

    def __str__(self):
        return f'Ordered_room : {self.ordered_room}, Guest : {self.guest_name}'