from django.db import models
from django.contrib.auth.models import User
from authentication.models import Specialist, Mother


class Appointment(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    specialist = models.ForeignKey(Specialist, related_name='specialist', on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey(Mother, related_name='doctor', on_delete=models.SET_NULL, null=True)

class AppointmentRequest(models.Model):
    from_mother = models.ForeignKey(Mother, related_name='from_mother', on_delete=models.CASCADE)
    to_doctor = models.ForeignKey(Specialist, related_name='to_doctor', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.from_mother.first_name