from django.contrib import admin
from .models import Guest,Room,Registration

class GuestAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'last_name', 'first_name', 'middle_name', 'city')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_count', 'floor', 'tv','fridge','bed_count','category','price_per_night')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_code', 'guest', 'arrival_date', 'stay_days', 'room')

admin.site.register(Guest, GuestAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Registration, RegistrationAdmin)
