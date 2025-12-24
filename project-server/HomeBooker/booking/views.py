from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Accommodation, Booking
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AccommodationForm, GuestSignUpForm, OwnerSignUpForm
from .forms import BookingForm



def accommodation_list(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'booking/accommodation_list.html', {'accommodations': accommodations})

@login_required
def add_accommodation(request):
    if request.user.role != 'owner':
        return redirect('/')  # запрет для не-владельцев

    if request.method == 'POST':
        form = AccommodationForm(request.POST, request.FILES)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.owner = request.user
            accommodation.save()
            return redirect('/')
    else:
        form = AccommodationForm()

    return render(request, 'booking/add_accommodation.html', {'form': form})



@login_required
def accommodation_detail(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.accommodation = accommodation
            booking.save()
            return redirect('accommodation_list')
    else:
        form = BookingForm()

    return render(request, 'booking/accommodation_detail.html', {
        'accommodation': accommodation,
        'form': form
    })


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('accommodation')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('my_bookings')
def register_guest(request):
    if request.method == 'POST':
        form = GuestSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = GuestSignUpForm()
    return render(request, 'booking/register.html', {'form': form, 'role': 'guest'})

def register_owner(request):
    if request.method == 'POST':
        form = OwnerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = OwnerSignUpForm()
    return render(request, 'booking/register.html', {'form': form, 'role': 'owner'})


@login_required
def edit_accommodation(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    if accommodation.owner != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = AccommodationForm(request.POST, request.FILES, instance=accommodation)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccommodationForm(instance=accommodation)

    return render(request, 'booking/edit_accommodation.html', {'form': form})


@login_required
def delete_accommodation(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    if accommodation.owner != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        accommodation.delete()
        return redirect('/')

    return render(request, 'booking/delete_confirm.html', {'accommodation': accommodation})