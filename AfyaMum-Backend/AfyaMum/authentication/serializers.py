from rest_framework import serializers
from .models import Specialist, Mother

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'clinic', 'speciality', 'gender', 'residence']

class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'clinic', 'gender', 'residence']

