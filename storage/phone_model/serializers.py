from rest_framework import serializers

from ..models import PhoneModel


class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('id', 'name', 'brand', 'model_year')


class PhoneModelFilterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    brand = serializers.CharField(required=False)

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
