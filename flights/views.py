from datetime import datetime

from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer , DetailSerializer,UpdateSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer



class BookingObjAPIView(RetrieveAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    serializer_class = DetailSerializer



class BookingObjUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    serializer_class = UpdateSerializer


class BookingDeleteApiview(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

    
