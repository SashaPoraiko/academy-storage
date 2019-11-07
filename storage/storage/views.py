from rest_framework import viewsets

from ..views import StorageAuthModelPaginateMixin, StorageAuthMixin
from ..models import Storage
from .serializers import StorageReadSerializer, StorageWriteSerializer, StorageFilterSerializer, StorageShortSerializer


class StorageViewSet(StorageAuthModelPaginateMixin):
    queryset = Storage.objects.all()
    serializer_class = StorageReadSerializer
    filter_serializer = StorageFilterSerializer
    serializer_map = {
        'create': StorageWriteSerializer,
        'update': StorageWriteSerializer,
    }


class StorageShortViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageShortSerializer
    filter_serializer = StorageShortSerializer
