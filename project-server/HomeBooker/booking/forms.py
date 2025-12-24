from django import forms
from .models import Accommodation
from .models import Booking
from .models import User
from django.contrib.auth.forms import UserCreationForm


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['name', 'description', 'price', 'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }


class GuestSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'guest'
        if commit:
            user.save()
        return user

class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'owner'
        if commit:
            user.save()
        return user