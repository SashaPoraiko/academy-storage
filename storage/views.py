from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Phone, Part, PhoneModel, Storage
from .serializers import UserSerializer, PhoneSerializer, PartSerializer, PhoneModelSerializer, StorageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
