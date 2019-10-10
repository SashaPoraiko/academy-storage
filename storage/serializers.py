from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import empty

from .models import Phone, Part, PhoneModel, Storage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('id', 'name', 'brand', 'model_year')


class PhoneSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    phone_model = PhoneModelSerializer()

    class Meta:
        model = Phone
        fields = ('id', 'phone_model', 'author', 'comment', 'date_release', 'date_create', 'date_modify')


class PartSerializer(serializers.ModelSerializer):
    phone_models = PhoneModelSerializer(many=True)

    class Meta:
        model = Part
        fields = ('id', 'name', 'condition', 'phone_models')


class PartWriteSerializer(serializers.ModelSerializer):
    phone_models = serializers.PrimaryKeyRelatedField(queryset=PhoneModel.objects.all(), many=True)

    class Meta:
        model = Part
        fields = ('name', 'condition', 'phone_models')


class StorageSerializer(serializers.ModelSerializer):
    part = PartSerializer()
    phone = PhoneSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'locker', 'row', 'column', 'part', 'phone')


class PhoneFilterSerializer(serializers.Serializer):
    comment = serializers.CharField(required=False)
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
