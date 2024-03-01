from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import BookingRoom


class BookingRoomListView(ListView):
    model = BookingRoom
    template_name = "pattern.html"
