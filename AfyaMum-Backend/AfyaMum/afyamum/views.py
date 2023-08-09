from django.shortcuts import render
from .models import Specialist, Mother, Appointment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import MotherSerializer, AppointmentSerializer, SpecialistSerializer, MotherSerializerWithToken, SpecialistSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MotherTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = MotherSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MotherTokenObtainPairView(TokenObtainPairView):
    serializer_class = MotherTokenObtainPairSerializer

class SpecialistTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = SpecialistSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class SpecialistTokenObtainPairView(TokenObtainPairView):
    serializer_class = SpecialistTokenObtainPairSerializer


@api_view(['POST'])
def registerMother(request):
    data = request.data
    try:
        mother = Mother.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password']),
            age = data['age'],
            phone_number=['phone_number'],
            residence=['residence']
        )

        serializer = MotherSerializer(Mother, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Mother with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registerSpecialist(request):
    data = request.data
    try:
        mother = Specialist.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password']),
            specialist = data['specialist'],
            start_time=['start_time'],
            end_time=['end_time'],
            gender=['gender']
        )

        serializer = SpecialistSerializer(Specialist, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Mother with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


