# booking/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import accommodation_list, add_accommodation, accommodation_detail, my_bookings, cancel_booking, \
    register_guest, register_owner

urlpatterns = [
    path('', accommodation_list, name='accommodation_list'),
    path('add/', add_accommodation, name='add_accommodation'),

    path('accommodation/<int:pk>/', accommodation_detail, name='accommodation_detail'),  # ← new

    path('my-bookings/', my_bookings, name='my_bookings'),
    
    path('cancel-booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),

    path('register/guest/', register_guest, name='register_guest'),
    path('register/owner/', register_owner, name='register_owner'),

    path('accommodation/<int:pk>/edit/', views.edit_accommodation, name='edit_accommodation'),
    path('accommodation/<int:pk>/delete/', views.delete_accommodation, name='delete_accommodation'),



]
