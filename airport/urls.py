"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights import views as flight_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", flight_views.FlightListView.as_view(), name="flights-list"),
    path("bookings/", flight_views.BookingListView.as_view(), name="bookings-list"),
    path ("booking-details/<int:booking_id>",flight_views.BookingObjAPIView.as_view()),
    path("update-booking/<int:booking_id>",flight_views.BookingObjUpdateView.as_view()),
    path("cancel-booking/<int:booking_id>",flight_views.BookingDeleteApiview.as_view()),
]
