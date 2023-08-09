from rest_framework import serializers
from core.models import Specialist, Mother, Appointment, AppointmentRequest

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = '__all__'

class MotherSerializerWithToken(MotherSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mother
        fields = ['username', 'email', 'phone_number']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class SpecialistSerializerWithToken(SpecialistSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Specialist
        fields = '__all_'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)