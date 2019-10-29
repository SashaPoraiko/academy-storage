from rest_framework import viewsets

from ..models import Part
from ..views import StorageAuthModelPaginateMixin, StorageAuthMixin

from .serializers import PartReadSerializer, PartFilterSerializer, PartWriteSerializer, PartShortSerializer


class PartViewSet(StorageAuthModelPaginateMixin):
    queryset = Part.objects.all()
    serializer_class = PartReadSerializer
    filter_serializer = PartFilterSerializer
    serializer_map = {
        'create': PartWriteSerializer,
        'update': PartWriteSerializer,
    }


class PartShortViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartShortSerializer
    filter_serializer = PartFilterSerializer
