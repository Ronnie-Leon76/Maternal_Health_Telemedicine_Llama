from django.urls import path
from .views import *
from .view_drf import *

urlpatterns = [
    
    # path('appointments/', AppointmentList.as_view()),
    # path('appointments/<int:pk>/', AppointmentDetail.as_view()),
    # path('appointmentrequest/', AppointmentRequestDetail.as_view()),
    # path('appointmentrequest/<int:pk>/', AppointmentRequestDetail.as_view()),

    path('sessions/', SessionList.as_view()),
    path('sessions/<int:pk>/', SessionDetail.as_view()),

    path('exchanges/', ExchangeList.as_view()),
    path('exchanges/<int:pk>/', ExchangeDetail.as_view()),
]
