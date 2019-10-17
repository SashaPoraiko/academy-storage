from django.contrib.auth.models import User

from rest_framework import viewsets

from storage.utils import parse_query_params
from .models import Phone, Part, PhoneModel, Storage
from .serializers import UserSerializer, PhoneReadSerializer, PartReadSerializer, PhoneModelSerializer, \
    StorageReadSerializer, \
    PhoneFilterSerializer, PartWriteSerializer, PhoneWriteSerializer, StorageWriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneReadSerializer

    def get_queryset(self):
 restpartfilter
        data = parse_query_params(
            self.request.query_params.copy(),
            (('date-create-from', 'date_create_from'),)
        )
        filter_serializer = PhoneFilterSerializer(data=data, context={'request': self.request})
        if filter_serializer.is_valid():
            return self.queryset.filter(**filter_serializer.validated_data)
        return self.queryset

    def create(self, request, *args, **kwargs):
        self.serializer_class = PhoneWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PhoneWriteSerializer
        return super().update(request, args, kwargs)




class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartReadSerializer

    def get_queryset(self):
        queryset = Part.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def create(self, request, *args, **kwargs):
        self.serializer_class = PartWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PartWriteSerializer
        return super().update(request, args, kwargs)


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        brand = self.request.query_params.get('brand')
        if brand:
            self.queryset = self.queryset.filter(brand__icontains=brand)

        return self.queryset


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageReadSerializer

    def get_queryset(self):
        column = self.request.query_params.get('column')
        row = self.request.query_params.get('row')
        locker = self.request.query_params.get('locker')
        if column:
            self.queryset = self.queryset.filter(column=column)
        if row:
            self.queryset = self.queryset.filter(row=row)
        if locker:
            self.queryset = self.queryset.filter(locker=locker)

        return self.queryset

    def create(self, request, *args, **kwargs):
        self.serializer_class = StorageWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = StorageWriteSerializer
        return super().update(request, args, kwargs)
