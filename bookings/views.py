from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Service
from .forms import BookingForm

def home(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Send email notification
            send_mail(
                subject=f'New Booking - {booking.customer_name}',
                message=f'''
New booking received at Serenity Spa!

Customer: {booking.customer_name}
Email: {booking.customer_email}
Phone: {booking.customer_phone}
Service: {booking.service.name}
Date: {booking.booking_date}
Time: {booking.booking_time}
Notes: {booking.notes}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/home.html', {'services': services, 'form': form})

def booking_success(request):
    return render(request, 'bookings/success.html')