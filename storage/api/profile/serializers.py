from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.fields import EmailField, CharField


class ForgotPasswordSerializer(serializers.Serializer):
    email = EmailField(required=True)


class ValidatePasswordSerializer(serializers.Serializer):
    password = CharField(required=True)
    password_confirm = CharField(required=True)

    def validate_password(self, value):
        password_validation.validate_password(value, self.context.get("user"))
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs['password'] != attrs['password_confirm']:
            message = 'Passwords do not match'
            raise serializers.ValidationError(
                {
                    "password": [message],
                    "password_confirm": [message],
                }
            )
        return attrs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'username', 'is_staff', 'is_active')
        fields = read_only_fields + ('email',)
