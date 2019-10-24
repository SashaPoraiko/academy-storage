from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Storage
from ..utils import parse_query_params

from .serializers import StorageReadSerializer, StorageWriteSerializer


class StorageAuthMixin(viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        filter_serializer = getattr(self, 'filter_serializer', None)

        if filter_serializer is None:
            return self.queryset

        data = parse_query_params(
            self.request.query_params,
            getattr(self, 'filter_parse_query_params', None)
        )
        filter_serializer = filter_serializer(data=data, context={'request': self.request})
        if filter_serializer.is_valid():
            return self.queryset.filter(**filter_serializer.validated_data)
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
