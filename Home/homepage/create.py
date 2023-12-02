from homepage.models import Guest, Room, Registration
from django.utils import timezone
import random

# Створіть гостей
guests_data = [
    {'last_name': 'Іванов', 'first_name': 'Іван', 'middle_name': 'Петрович', 'city': 'Київ'},
    {'last_name': 'Петров', 'first_name': 'Петро', 'middle_name': 'Іванович', 'city': 'Львів'},
    {'last_name': 'Сидоров', 'first_name': 'Сидір', 'middle_name': 'Васильович', 'city': 'Харків'},
    {'last_name': 'Коваленко', 'first_name': 'Олена', 'middle_name': 'Андріївна', 'city': 'Дніпро'},
    {'last_name': 'Михайленко', 'first_name': 'Михайло', 'middle_name': 'Ігорович', 'city': 'Одеса'},
    {'last_name': 'Козлов', 'first_name': 'Анна', 'middle_name': 'Володимирівна', 'city': 'Львів'},
    {'last_name': 'Шевченко', 'first_name': 'Тарас', 'middle_name': 'Григорович', 'city': 'Київ'},
]

for guest_data in guests_data:
    Guest.objects.create(**guest_data)

# Створіть номери
rooms_data = [
    {'number': 101, 'room_count': 2, 'floor': 1, 'tv': True, 'fridge': True, 'bed_count': 2, 'category': 'звичайний', 'price_per_night': 1000},
    {'number': 102, 'room_count': 1, 'floor': 1, 'tv': False, 'fridge': True, 'bed_count': 1, 'category': 'полу люкс', 'price_per_night': 1500},
    {'number': 201, 'room_count': 3, 'floor': 2, 'tv': True, 'fridge': False, 'bed_count': 3, 'category': 'люкс', 'price_per_night': 2000},
    {'number': 202, 'room_count': 1, 'floor': 2, 'tv': True, 'fridge': True, 'bed_count': 1, 'category': 'звичайний', 'price_per_night': 1200},
    {'number': 301, 'room_count': 2, 'floor': 3, 'tv': False, 'fridge': False, 'bed_count': 2, 'category': 'полу люкс', 'price_per_night': 1600},
    {'number': 302, 'room_count': 2, 'floor': 3, 'tv': True, 'fridge': True, 'bed_count': 2, 'category': 'звичайний', 'price_per_night': 1100},
    {'number': 401, 'room_count': 1, 'floor': 4, 'tv': True, 'fridge': False, 'bed_count': 1, 'category': 'полу люкс', 'price_per_night': 1800},
    {'number': 402, 'room_count': 3, 'floor': 4, 'tv': True, 'fridge': True, 'bed_count': 3, 'category': 'люкс', 'price_per_night': 2200},
    {'number': 501, 'room_count': 1, 'floor': 5, 'tv': False, 'fridge': True, 'bed_count': 1, 'category': 'звичайний', 'price_per_night': 1300},
    {'number': 502, 'room_count': 2, 'floor': 5, 'tv': True, 'fridge': False, 'bed_count': 2, 'category': 'полу люкс', 'price_per_night': 1700},
]

for room_data in rooms_data:
    Room.objects.create(**room_data)

# Створіть реєстрації гостей
registrations_data = []
for _ in range(10):
    guest = random.choice(Guest.objects.all())
    room = random.choice(Room.objects.all())
    arrival_date = timezone.now()
    stay_days = random.randint(1, 7)
    registrations_data.append({'guest': guest, 'arrival_date': arrival_date, 'stay_days': stay_days, 'room': room})

for registration_data in registrations_data:
    Registration.objects.create(**registration_data)
