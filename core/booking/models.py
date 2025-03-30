from django.contrib.auth.models import User
from django.db import models


# TODO допиши бд

class Room(models.Model):

    number = models.CharField(max_length=10, unique=True)
    type = ...
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Комната {self.number} ({self.type})'


class Booking(models.Model):
    user = models.ForeignKey(...)
    room = models.ForeignKey(...)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['room', 'check_in', 'check_out']

    def __str__(self):
        return f'{self.user} забронировал {self.room} с {self.check_in} по {self.check_out}'
