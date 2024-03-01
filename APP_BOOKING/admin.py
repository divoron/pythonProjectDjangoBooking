from django.contrib import admin

# Register your models here.

from .models import BookingRoom

admin.site.register(BookingRoom)