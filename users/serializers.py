from rest_framework import serializers
from . import models
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'name' )