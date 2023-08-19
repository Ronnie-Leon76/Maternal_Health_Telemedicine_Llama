from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# from authentication.models import Specialist, Mother

class Speciality(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, related_name='profile')
    specialities = models.ManyToManyField(Speciality, blank=True)
    is_mother = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
    
class Session(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='sessions')
    date_posted = models.DateTimeField(auto_now_add=True)

class Exchange(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="exchanges")
    body = models.TextField()
    is_bot = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# class Appointment(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     specialist = models.ForeignKey(Specialist, related_name='specialist', on_delete=models.SET_NULL, null=True)
#     mother = models.ForeignKey(Mother, related_name='doctor', on_delete=models.SET_NULL, null=True)

# class AppointmentRequest(models.Model):
#     from_mother = models.ForeignKey(Mother, related_name='from_mother', on_delete=models.CASCADE)
#     to_doctor = models.ForeignKey(Specialist, related_name='to_doctor', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_accepted = models.BooleanField(default=False)
#     def __str__(self):
#         return self.from_mother.first_name