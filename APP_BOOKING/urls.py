from django.urls import path

from .views import BookingRoomListView, hello_guest

urlpatterns = [
    path("", BookingRoomListView.as_view(), name="booking"),
    path("hello/", hello_guest)
]
