from django.db import transaction
from rest_framework import serializers

from storage.models import Device


class DeviceWriteMixin(serializers.ModelSerializer):

    @transaction.atomic
    def create(self, validated_data):
        instance = super().create(validated_data)
        params = {self.Meta.model.__name__.lower(): instance}
        Device(**params).save()
        return instance
