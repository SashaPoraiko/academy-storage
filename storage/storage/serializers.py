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


class StorageShortSerializer(serializers.ModelSerializer):
    part = PartReadSerializer()
    phone = PhoneReadSerializer()

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'part', 'phone')


class StorageWriteSerializer(serializers.ModelSerializer):
    part = serializers.PrimaryKeyRelatedField(queryset=Part.objects.all())
    phone = serializers.PrimaryKeyRelatedField(queryset=Phone.objects.all())

    class Meta:
        model = Storage
        fields = ('locker', 'row', 'column', 'part', 'phone')

    def to_representation(self, instance):
        return PartReadSerializer(instance).data


class StorageFilterSerializer(serializers.Serializer):
    # todo fields
    locker = serializers.CharField(required=False)
    row = serializers.IntegerField(required=False)
    column = serializers.IntegerField(required=False)

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
