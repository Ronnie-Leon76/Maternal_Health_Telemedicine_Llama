from rest_framework import serializers
from .models import Specialist, Mother, Appointment, AppointmentRequest

class AppointmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRequest
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

        def get_appointmentsrequests(self, obj):
            appointmentrequests = obj.appointmentrequests_set.all()
            serializer = AppointmentRequestSerializer(appointmentrequests, many=True)
            return serializer.data