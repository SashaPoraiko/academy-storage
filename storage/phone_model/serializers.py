from rest_framework import serializers

from ..models import PhoneModel


class PhoneModelShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('id', 'name')


class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('id', 'name', 'brand', 'model_year')


class PhoneModelFilterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=80)
    brand = serializers.CharField(required=False, max_length=30)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        filters = {}

        name = attrs.get('name')
        if name:
            filters['name__icontains'] = name

        brand = attrs.get('brand')
        if brand:
            filters['brand__icontains'] = brand

        return filters
