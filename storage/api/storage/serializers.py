from rest_framework import serializers

from storage.models import Storage, Device
from ..device.serializers import DeviceReadSerializer


class StorageReadSerializer(serializers.ModelSerializer):
    device = DeviceReadSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'locker', 'row', 'column', 'device')


class StorageShortSerializer(serializers.ModelSerializer):
    device = DeviceReadSerializer()

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'device')


class StorageWriteSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'device')

    def to_representation(self, instance):
        return StorageReadSerializer(instance).data


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
