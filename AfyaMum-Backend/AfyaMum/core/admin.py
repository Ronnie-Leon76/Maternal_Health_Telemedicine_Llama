from django.contrib import admin
from .models import Appointment, AppointmentRequest


admin.site.register(Appointment)
admin.site.register(AppointmentRequest)