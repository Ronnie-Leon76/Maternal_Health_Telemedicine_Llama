from django.urls import path

from .views import prompt

urlpatterns = [
    path('bot/', prompt),
]
