from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# from .models import Appointment, AppointmentRequest
from .permission import IsOwnerOrReadOnly
# from .serializers import AppointmentSerializer, AppointmentRequestSerializer

# class AppointmentList(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.reques.user)

#     def get(self, request: Request, *args, **kwargs) -> Response:
#         return self.list(request, *args, **kwargs)

#     def post(self, request: Request, *args, **kwargs) -> Response:
#         return self.create(request, *args, **kwargs)

# class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

#     def get(self, request: Request, *args, **kwargs) -> Response:
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request: Request, *args, **kwargs) -> Response:
#         user = self.request.user
#         appointment = self.get_object()
#         if user != appointment.mother:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         else:
#             return self.update(request, *args, **kwargs)

#     def delete(self, request: Request, *args, **kwargs) -> Response:
#         user = self.request.user
#         appointment = self.get_object()
#         if user != appointment.mother:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         else:
#             return self.destroy(request, *args, **kwargs)

# class AppointmentRequestList(generics.ListCreateAPIView):
#     queryset = AppointmentRequest.objects.all()
#     serializer_class = AppointmentRequestSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
           
#     def get(self, request: Request, *args, **kwargs) -> Response:
#         specialist = self.request.user
#         if specialist:
#             return self.list(request, *args, **kwargs)
#         else:
#             return Response(status=status.HTTP_403_FORBIDDEN)
    
#     def post(self, request: Request, *args, **kwargs) -> Response:
#         return self.create(request, *args, **kwargs)
        
# class AppointmentRequestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AppointmentRequest.objects.all()
#     serializer_class = AppointmentRequestSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
#     def get(self, request: Request, *args, **kwargs) -> Response:
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request: Request, *args, **kwargs) -> Response:
#         specialist = self.request.user
#         appointment_request = self.get_object()
#         if user != appointment_request.mother:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         else:
#             return self.update(request, *args, **kwargs)
    
#     def delete(self, request: Request, *args, **kwargs) -> Response:
#         specialist = self.request.user
#         appointment_request = self.get_object()
#         if user != appointment_request.mother:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         else:
#             return self.destroy(request, *args, **kwargs)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def accept_appointment_request(request, appointment_id, mother_id):
#     user = request.user
#     mother = get_object_or_404(Mother, id=mother_id)
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     if user != appointment.specialist:
#         return Response(status=403)
#     appointment.update(is_accepted=True)
#     # Trigger SIgnal
#     return Response('Appointment request accepted')