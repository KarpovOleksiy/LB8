from django.shortcuts import render
from .models import Guest, Room, Registration

def home(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    registrations = Registration.objects.all()
    
    return render(request, 'index.html', {'guests': guests, 'rooms': rooms, 'registrations': registrations})
