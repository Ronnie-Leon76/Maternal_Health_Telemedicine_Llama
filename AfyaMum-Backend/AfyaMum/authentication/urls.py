from django.urls import path
from .views import *

urlpatterns = [
    path('login-as-mum/', MotherTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login-as-specialist/', SpecialistTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register-as-mum/', registerMother, name='register'),
    path('register-as-specialist/', registerSpecialist, name='register'),

]