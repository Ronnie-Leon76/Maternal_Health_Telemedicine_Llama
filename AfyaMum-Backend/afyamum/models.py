from django.db import models
from django.contrib.auth.models import user

class Mother(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    residence = models.CharField(max_length=30)

    class Meta:
        ordering = ['phone_number']

    def __str__(self):
        return self.phone_number

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    gender = models.CharField(max_length=30)

    class Meta:
        ordering = ['phone_number']

    def __str__(self):
        return self.phone_number


class Appointment(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    specialist = models.ForeignKey(Specialist, related_name='specialist', on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey(Doctor, related_name='doctor', on_delete=models.SET_NULL, null=True)
