from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('<str:room>/', views.room, name="Room"),
    path('check_room', views.check_rooms, name="Check_rooms"),
    path('send', views.send, name="Send"),
    path('getMessages/<str:room>/', views.getMessages, name="Get_messages")
]