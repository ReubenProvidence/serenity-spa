from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone',
                  'service', 'booking_date', 'booking_time', 'notes']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'customer_phone': 'Phone Number',
            'service': 'Select Service',
            'booking_date': 'Preferred Date',
            'booking_time': 'Preferred Time',
            'notes': 'Special Requests (Optional)',
        }