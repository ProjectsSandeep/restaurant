from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart', views.cart, name="cart"),
    path('menu', views.menu, name="menu"),
    path('events', views.events, name="events"),
    path('place_order', views.place_order, name="place_order"),
    path('reserve_table', views.reserve_table, name="reserve_table")
]