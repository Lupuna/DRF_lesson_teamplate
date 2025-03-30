from rest_framework import serializers
from .models import User, Room, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = ...

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        ...