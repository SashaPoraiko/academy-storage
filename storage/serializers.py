from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Phone


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff','id']


class PhoneSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Phone
        fields = ('phone_model', 'author', 'comment', 'date_release', 'date_create', 'date_modify')
