from django.core.validators import MinValueValidator
from rest_framework import serializers

from ..models import Storage, Part, Phone, Device
from ..part.serializers import PartReadSerializer
from ..phone.serializers import PhoneReadSerializer


class DeviceReadSerializer(serializers.ModelSerializer):
    part = PartReadSerializer()
    phone = PhoneReadSerializer()

    class Meta:
        model = Device
        fields = ('id', 'part', 'phone')

