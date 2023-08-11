from rest_framework import serializers
# from .models import Specialist, Mother

# class SpecialistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Specialist
#         fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'clinic', 'speciality', 'gender', 'residence']

# class MotherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mother
#         fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'clinic', 'gender', 'residence']

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

# TODO rest_framework\authtoken\serializers.py
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    profile_id = serializers.IntegerField(source="profile.id")

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'profile_id']

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        source="key",
        read_only=True
    )
    user = UserProfileSerializer(required=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

