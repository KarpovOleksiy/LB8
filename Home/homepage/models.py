from django.db import models

class Guest(models.Model):
    registration_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Room(models.Model):
    number = models.IntegerField(primary_key=True)
    room_count = models.IntegerField()
    floor = models.IntegerField()
    tv = models.BooleanField()
    fridge = models.BooleanField()
    bed_count = models.IntegerField()
    CATEGORY_CHOICES = [
        ('звичайний', 'Звичайний'),
        ('полу люкс', 'Полу Люкс'),
        ('люкс', 'Люкс'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='звичайний')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Номер {self.number}'


class Registration(models.Model):
    registration_code = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, to_field='registration_number')
    arrival_date = models.DateField()
    stay_days = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guest} - {self.arrival_date}'
