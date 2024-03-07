from django.contrib import admin

# Register your models here.

from .models import BookingRoom
from .models import Guest

admin.site.register(BookingRoom)
admin.site.register(Guest)
