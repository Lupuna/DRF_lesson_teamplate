from rest_framework import viewsets, permissions
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from .permissions import IsOwnerOrReadOnly


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.filter(is_available=True)
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        ...

    def perform_create(self, serializer):
        ...