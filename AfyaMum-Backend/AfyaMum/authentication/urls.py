from django.urls import path
from .views import *

urlpatterns = [
    # # User registration endpoints
    # path('signup/mother/', MotherRegistrationView.as_view(), name='mother-signup'),
    # path('signup/specialist/', SpecialistRegistrationView.as_view(), name='specialist-signup'),
    
    # # User login endpoint
    # path('login/', UserLoginView.as_view(), name='user-login'),

    path('register/v2', register, name='register'),

]

# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

from . import view_drf
urlpatterns += [
    path('api-token-auth/v2/', view_drf.obtain_auth_token)
]