from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Кастомный пользователь с ролью
class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('owner', 'Owner'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# Жильё
class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accommodations')

    image = models.ImageField(upload_to='accommodation_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.location})"




class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accommodation = models.ForeignKey('Accommodation', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.accommodation.name}"

