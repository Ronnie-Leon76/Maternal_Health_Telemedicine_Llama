from django.urls import path
from .views import *

urlpatterns = [
    path('login-as-mum/', MotherTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login-as-specialist/', SpecialistTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register-as-mum/', registerMother, name='register'),
    path('register-as-specialist/', registerSpecialist, name='register'),
    path('appointments/', AppointmentList.as_view()),
    path('appointments/<int:pk>/', AppointmentDetail.as_view()),
    path('appointmentrequest/', AppointmentRequestDetail.as_view()),
    path('appointmentrequest/<int:pk>/', AppointmentRequestDetail.as_view()),

]