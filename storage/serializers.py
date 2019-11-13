from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'username', 'is_staff', 'is_active')
        fields = read_only_fields + ('email',)
