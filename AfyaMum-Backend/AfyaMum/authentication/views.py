from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from .models import Mother, Specialist
from .serializers import MotherSerializer, SpecialistSerializer
from django.contrib.auth.hashers import make_password

@permission_classes([AllowAny])
class MotherRegistrationView(generics.CreateAPIView):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        validate_password(password)
        mother = serializer.save()
        mother.set_password(password)
        mother.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class SpecialistRegistrationView(generics.CreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        validate_password(password)
        specialist = serializer.save()
        specialist.set_password(password)
        specialist.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class UserLoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
