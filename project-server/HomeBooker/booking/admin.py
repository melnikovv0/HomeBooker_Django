from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Accommodation, Booking

admin.site.register(User)
admin.site.register(Accommodation)
admin.site.register(Booking)