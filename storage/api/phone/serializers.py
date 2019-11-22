from rest_framework import serializers

from storage.models import PhoneModel, Phone
from ..device.mixins import DeviceWriteMixin
from ..phone_model.serializers import PhoneModelSerializer
from ..profile.serializers import UserSerializer


class PhoneShortSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = ('id', 'name')

    @classmethod
    def get_name(cls, instance):
        return f'{instance.phone_model} {instance.condition}'


class PhoneReadSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    phone_model = PhoneModelSerializer()

    class Meta:
        model = Phone
        fields = ('id', 'phone_model', 'author', 'comment', 'date_release', 'date_create', 'date_modify', 'device')


class PhoneWriteSerializer(DeviceWriteMixin):
    phone_model = serializers.PrimaryKeyRelatedField(queryset=PhoneModel.objects.all())

    class Meta:
        model = Phone
        fields = ('phone_model', 'author', 'comment', 'date_release', 'date_create', 'date_modify')

    def to_representation(self, instance):
        return PhoneReadSerializer(instance).data


class PhoneFilterSerializer(serializers.Serializer):
    comment = serializers.CharField(required=False, max_length=80)
    model = serializers.IntegerField(required=False, min_value=1)
    date_create_from = serializers.DateField(required=False, input_formats=['iso-8601'])
    date_create_to = serializers.DateField(required=False, input_formats=['iso-8601'])

    def validate(self, attrs):

        attrs = super().validate(attrs)

        filters = {}

        comment = attrs.get('comment')
        if comment:
            filters['comment__icontains'] = comment

        model = attrs.get('model')
        if model:
            filters['phone_model'] = model

        date_create_from = attrs.get('date_create_from')
        date_create_to = attrs.get('date_create_to')

        if date_create_from and date_create_to:
            filters['date_create__range'] = [date_create_from, date_create_to]
        else:
            if date_create_from:
                filters['date_create__gte'] = date_create_from

            if date_create_to:
                filters['date_create__lte'] = date_create_to

        return filters
