from django.urls import path
from .views import *

urlpatterns = [
    # User registration endpoints
    path('signup/mother/', MotherRegistrationView.as_view(), name='mother-signup'),
    path('signup/specialist/', SpecialistRegistrationView.as_view(), name='specialist-signup'),
    
    # User login endpoint
    path('login/', UserLoginView.as_view(), name='user-login'),

]