from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.booking_success, name='booking_success'),
]