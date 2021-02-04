from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()) #if it gets this url, it will give a view off RoomView class
]