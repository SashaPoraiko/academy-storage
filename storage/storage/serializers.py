
from rest_framework import serializers

from ..models import Storage, Part, Phone
from ..part.serializers import PartReadSerializer
from ..phone.serializers import PhoneReadSerializer


class StorageReadSerializer(serializers.ModelSerializer):
    part = PartReadSerializer()
    phone = PhoneReadSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'locker', 'row', 'column', 'part', 'phone')


class StorageWriteSerializer(serializers.ModelSerializer):
    part = serializers.PrimaryKeyRelatedField(queryset=Part.objects.all())
    phone = serializers.PrimaryKeyRelatedField(queryset=Phone.objects.all())

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'part', 'phone')

    def to_representation(self, instance):
        return PartReadSerializer(instance).data
