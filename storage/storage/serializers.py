from django.core.validators import MinValueValidator
from rest_framework import serializers

from storage.device.serializers import DeviceReadSerializer
from ..models import Storage, Part, Phone, Device
from ..part.serializers import PartReadSerializer
from ..phone.serializers import PhoneReadSerializer


class StorageReadSerializer(serializers.ModelSerializer):
    # part = PartReadSerializer()
    # phone = PhoneReadSerializer()
    device = DeviceReadSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'locker', 'row', 'column', 'device')


class StorageShortSerializer(serializers.ModelSerializer):
    # part = PartReadSerializer()
    # phone = PhoneReadSerializer()
    device = DeviceReadSerializer()

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'device')


class StorageWriteSerializer(serializers.ModelSerializer):
    # part = serializers.PrimaryKeyRelatedField(queryset=Part.objects.all())
    # phone = serializers.PrimaryKeyRelatedField(queryset=Phone.objects.all())
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'device')

    # def to_representation(self, instance):
    #     return PartReadSerializer(instance).data


class StorageFilterSerializer(serializers.Serializer):
    locker = serializers.CharField(required=False, max_length=80)
    row = serializers.IntegerField(required=False, min_value=1, max_value=10)
    column = serializers.IntegerField(required=False, min_value=1, max_value=10)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        filters = {}

        column = attrs.get('column')
        if column:
            filters['column'] = column

        row = attrs.get('row')
        if row:
            filters['row'] = row

        locker = attrs.get('locker')
        if locker:
            filters['locker'] = locker

        return filters
