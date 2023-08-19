

# TODO https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#pulling-it-all-together
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, date #timezone

from django.http import Http404
from rest_framework.views import APIView

# TODO https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#adding-optional-format-suffixes-to-our-urls
from django.db.models import Q, ProtectedError

from rest_framework import generics
from rest_framework.exceptions import PermissionDenied, ParseError, ValidationError

import requests
import json

from core.models import Profile

from .models import (Session, Exchange)
from .serializers import (SessionSerializer, ExchangeSerializer)

# ! SESSION
class SessionList(generics.ListCreateAPIView):
    """
    List all Session or create a new Session.
    """    
    # pagination_class = CustomPagination

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Session.objects.filter(creator=self.request.user).order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        date_posted = self.request.query_params.get('date_posted')
        if date_posted:
            queryset = queryset.filter(date_posted=date_posted)

        return queryset

    def get_serializer_class(self):
        return SessionSerializer

    def perform_create(self, serializer):
        instance = serializer.save(creator=self.request.user)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a Session
    """

    def get_serializer_class(self):
        return SessionSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Session.objects.all()
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()

# ! EXCHANGE
class ExchangeList(generics.ListCreateAPIView):
    """
    List all Exchange or create a new Exchange.
    """
    
    # pagination_class = CustomPagination

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Exchange.objects.filter(session__creator=self.request.user).order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        session = self.request.query_params.get('session')
        if session:
            queryset = queryset.filter(session=session)

        return queryset

    def get_serializer_class(self):
        return ExchangeSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        url = 'https://082f-34-76-51-85.ngrok-free.app/bot/bot/'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "prompt" : instance.body
        }

        r = requests.post(url, data=json.dumps(payload), headers=headers)
        response = r.json()
        data = {
            "body": response["result"],
            "session": instance.session.id,
            "is_bot": True,
        }
        serializer = ExchangeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        print(r.json())


class ExchangeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a Exchange
    """

    def get_serializer_class(self):
        return ExchangeSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Exchange.objects.all()
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()

# TODO https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#creating-an-endpoint-for-the-root-of-our-api
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'session': reverse('ecommerce:session-list', request=request, format=format),
        'exchanges': reverse('ecommerce:exchange-list', request=request, format=format),
    })