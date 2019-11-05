from rest_framework import serializers

from ..models import Part, PhoneModel
from ..phone_model.serializers import PhoneModelSerializer


class PartShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name')


class PartReadSerializer(serializers.ModelSerializer):
    phone_models = PhoneModelSerializer(many=True)

    class Meta:
        model = Part
        fields = ('id', 'name', 'condition', 'phone_models')


class PartWriteSerializer(serializers.ModelSerializer):
    phone_models = serializers.PrimaryKeyRelatedField(queryset=PhoneModel.objects.all(), many=True)

    class Meta:
        model = Part
        fields = ('name', 'condition', 'phone_models')

    def to_representation(self, instance):
        return PartReadSerializer(instance).data


class PartFilterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=80)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        filters = {}

        name = attrs.get('name')
        if name:
            filters['name__icontains'] = name
        return filters
