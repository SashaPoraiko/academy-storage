from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Phone, Part, PhoneModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('id', 'name', 'brand', 'model_year')


class PhoneSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    phone_model = PhoneModelSerializer()

    class Meta:
        model = Phone
        fields = ('id', 'phone_model', 'author', 'comment', 'date_release', 'date_create', 'date_modify')


class PartSerializer(serializers.ModelSerializer):
    phone_models = PhoneModelSerializer(many=True)

    class Meta:
        model = Part
        fields = ('id', 'name', 'condition', 'phone_models')
