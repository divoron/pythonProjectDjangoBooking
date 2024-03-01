from django.urls import path

from .views import BookingRoomListView

urlpatterns = [
   path("", BookingRoomListView.as_view(), name="booking"),
]
