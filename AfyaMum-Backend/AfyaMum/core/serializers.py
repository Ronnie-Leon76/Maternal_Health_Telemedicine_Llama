from rest_framework import serializers
# from .models import Specialist, Mother, Appointment, AppointmentRequest
from .models import Session, Exchange

# class AppointmentRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AppointmentRequest
#         fields = '__all__'

# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

#         def get_appointmentsrequests(self, obj):
#             appointmentrequests = obj.appointmentrequests_set.all()
#             serializer = AppointmentRequestSerializer(appointmentrequests, many=True)
#             return serializer.data

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'creator', 'date_posted']
        read_only_fields = ['creator']

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['id', 'session', 'body', 'is_bot', 'date_posted']