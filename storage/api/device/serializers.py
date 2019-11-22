from rest_framework import serializers

from storage.models import Device
from ..part.serializers import PartShortSerializer
from ..phone.serializers import PhoneShortSerializer


class DeviceReadSerializer(serializers.ModelSerializer):
    part = PartShortSerializer()
    phone = PhoneShortSerializer()

    class Meta:
        model = Device
        fields = ('id', 'part', 'phone')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['name'] = f'{represent["part"]["name"]} (part)' \
            if instance.part else f'{represent["phone"]["name"]} (phone)'
        return represent
