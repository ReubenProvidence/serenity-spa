from django.contrib import admin
from .models import Service, Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_minutes', 'price']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'service', 'booking_date', 'booking_time', 'status', 'created_at']
    list_filter = ['status', 'booking_date', 'service']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']
    readonly_fields = ['created_at']
    list_editable = ['status']