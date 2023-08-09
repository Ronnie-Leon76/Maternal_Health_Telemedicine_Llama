from django.shortcuts import render
from .models import Specialist, Mother, Appointment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def registerMother(request):
    data = request.data
    try:
        user = Mother.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password']),
            age = data['age'],
            phone_number=['phone_number'],
            residence=['residence']
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)