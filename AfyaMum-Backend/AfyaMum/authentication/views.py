from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

# from .models import Mother, Specialist
# from .serializers import MotherSerializer, SpecialistSerializer
from django.contrib.auth.hashers import make_password

import json

@csrf_exempt
def register(request):
    # pass
    if request.method=="POST":
        if request.body:
            if request.POST: # form
                data = request.POST.copy()
                data.pop('csrfmiddlewaretoken', None)
            else: # ajax json
                data = json.loads(request.body)

            if User.objects.filter(username__iexact=data.get('username')).exists():
                response = HttpResponse("User already exists")
                response.status_code = 400 # + https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse.status_code
                return response

            form = UserCreationForm(data)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                response = JsonResponse({
                    'username': username
                }, status=201)
                return response
            else:
                # + https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form.errors
                response = JsonResponse(form.errors, status=400)
                return response
        else:
            response = JsonResponse({
            "username": "username is required",
            "password": "password is required",
            },
            status=400)
            return response
                    
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html' , {'f_register': form} )

# @permission_classes([AllowAny])
# class MotherRegistrationView(generics.CreateAPIView):
#     queryset = Mother.objects.all()
#     serializer_class = MotherSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         password = serializer.validated_data.pop('password')
#         validate_password(password)
#         mother = serializer.save()
#         mother.set_password(password)
#         mother.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @permission_classes([AllowAny])
# class SpecialistRegistrationView(generics.CreateAPIView):
#     queryset = Specialist.objects.all()
#     serializer_class = SpecialistSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         password = serializer.validated_data.pop('password')
#         validate_password(password)
#         specialist = serializer.save()
#         specialist.set_password(password)
#         specialist.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @permission_classes([AllowAny])
# class UserLoginView(generics.CreateAPIView):

#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
