from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Phone
from .serializers import UserSerializer, PhoneSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
