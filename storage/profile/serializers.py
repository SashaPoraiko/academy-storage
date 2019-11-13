from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import EmailField


class ForgotPasswordSerializer(serializers.Serializer):
    email = EmailField(required=True)
